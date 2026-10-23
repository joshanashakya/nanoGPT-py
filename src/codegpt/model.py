import torch
import torch.nn as nn
from torch.nn import functional as F

from src.codegpt.gptconfig import GPT_CONFIG


class CausalSelfAttention(nn.Module):
    def __init__(self, config: dict):
        """
        Initializes multi-head self-attention that only looks at earlier tokens.
        Args:
            config (dict): Model configuration (embedding_dim, num_heads, context_length).
        """
        super().__init__()
        # batch_first tells the tensor has the batch dimension first (batch, sequence, embedding_dim)
        self.attention = nn.MultiheadAttention(config["embedding_dim"], config["num_heads"], batch_first=True)

        # True above the diagonal = "may not attend to future tokens".
        mask = torch.ones(config["context_length"], config["context_length"], dtype=torch.bool)

        # Register the causal mask as a buffer so it is saved and moved with the model, but not treated as a parameter.
        # It never changes during training. The rule "don't look at the future" is fixed, not learned.
        self.register_buffer("causal_mask", torch.triu(mask, diagonal=1))

    def forward(self, x):
        """
        Args:
            x (torch.Tensor): Token representations, shape (batch, sequence, embedding_dim).
        Returns:
            torch.Tensor: Updated representations, same shape as x.
        """
        # reads how many tokens are in the input, so the mask can be cut to fit
        sequence_length = x.size(1)

        mask = self.causal_mask[:sequence_length, :sequence_length]

        # x, x, x are query, key and value 
        output, _ = self.attention(x, x, x, attn_mask=mask, need_weights=False)

        return output


class FeedForward(nn.Module):
    def __init__(self, config: dict):
        """
        Initializes the position-wise feed-forward network.
        Args:
            config (dict): Model configuration (embedding_dim).
        """
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(config["embedding_dim"], 4 * config["embedding_dim"]), # 384 → 1536
            nn.GELU(),
            nn.Linear(4 * config["embedding_dim"], config["embedding_dim"]), # 1536 → 384
        )

    def forward(self, x):
        """
        Args:
            x (torch.Tensor): Token representations, shape (batch, sequence, embedding_dim).
        Returns:
            torch.Tensor: Updated representations, same shape as x.
        """
        return self.network(x)


class TransformerBlock(nn.Module):
    def __init__(self, config: dict):
        """
        Initializes one pre-LayerNorm Transformer block: attention, then feed-forward.
        Args:
            config (dict): Model configuration.
        """
        super().__init__()
        self.ln1 = nn.LayerNorm(config["embedding_dim"])
        self.attention = CausalSelfAttention(config)
        self.ln2 = nn.LayerNorm(config["embedding_dim"])
        self.feed_forward = FeedForward(config)

    def forward(self, x):
        """
        Args:
            x (torch.Tensor): Token representations, shape (batch, sequence, embedding_dim).
        Returns:
            torch.Tensor: Updated representations, same shape as x.
        """
        # 1. Attention sublayer
        # normalize before sending to attention
        normalized = self.ln1(x)    

        # gather context from earlier tokens
        attention_output = self.attention(normalized)  

        # residual: add to the original x
        x = x + attention_output         

        # 2. Feed-forward sublayer
        # normalize before sending to feed-forward
        normalized = self.ln2(x)        

        # process each token on its own              
        feed_forward_output = self.feed_forward(normalized)  

        # residual: add to the original x
        x = x + feed_forward_output                   

        return x


class GPTLanguageModel(nn.Module):
    def __init__(self, config: dict):
        super().__init__()
        self.config = config
        self.token_embedding = nn.Embedding(config["vocab_size"], config["embedding_dim"])

        # Ablation: the model can be built without position embeddings.
        if config["use_position_embeddings"]:
            self.position_embedding = nn.Embedding(config["context_length"], config["embedding_dim"])
        else:
            self.position_embedding = None

        self.blocks = nn.Sequential(*[TransformerBlock(config) for _ in range(config["num_layers"])])
        self.final_layer_norm = nn.LayerNorm(config["embedding_dim"])
        self.lm_head = nn.Linear(config["embedding_dim"], config["vocab_size"], bias=False)

        # Share token embeddings with the output projection.
        self.lm_head.weight = self.token_embedding.weight

        self.apply(self._init_weights)

    def _init_weights(self, module):
        """Small random starting weights, as in GPT-2."""
        if isinstance(module, (nn.Linear, nn.Embedding)):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)
        if isinstance(module, nn.Linear) and module.bias is not None:
            nn.init.zeros_(module.bias)

    def forward(self, input_ids, targets=None):
        """
        A method that will be called implicitly to return model outputs.
        Args:
            input_ids (torch.Tensor): Token ids, shape (batch, sequence).
            targets (torch.Tensor, optional): The next token at each position, same shape.
        Returns:
            tuple: logits of shape (batch, sequence, vocab_size), and the
                cross-entropy loss (None when no targets are given).
        """
        sequence_length = input_ids.size(1)
        if sequence_length > self.config["context_length"]:
            raise ValueError(f"Sequence length {sequence_length} exceeds context length {self.config['context_length']}")

        x = self.token_embedding(input_ids)
        if self.position_embedding is not None:
            positions = torch.arange(sequence_length, device=input_ids.device)
            x = x + self.position_embedding(positions)

        x = self.blocks(x)
        x = self.final_layer_norm(x)
        logits = self.lm_head(x)

        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.reshape(-1, logits.size(-1)), targets.reshape(-1))

        return logits, loss

    @torch.no_grad()
    def generate(self, input_ids, max_new_tokens, temperature=1.0, top_k=None):
        """
        Generates tokens one at a time, each conditioned on everything before it.
        Args:
            input_ids (torch.Tensor): Prompt token ids, shape (batch, sequence).
            max_new_tokens (int): How many tokens to add.
            temperature (float): Higher = more random, lower = more predictable.
            top_k (int, optional): Sample only from the k most likely tokens.
        Returns:
            torch.Tensor: The prompt followed by the generated tokens.
        """

        self.eval()
        for _ in range(max_new_tokens):
            # Keep only the most recent context window.
            input_context = input_ids[:, -self.config["context_length"]:]
            logits, _ = self(input_context)

            # Use logits for the last position.
            logits = logits[:, -1, :] / temperature

            # Keep only the top_k most likely tokens.
            if top_k is not None:
                values, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                logits[logits < values[:, [-1]]] = -float("inf")

            probabilities = F.softmax(logits, dim=-1)
            next_token = torch.multinomial(probabilities, num_samples=1)
            input_ids = torch.cat((input_ids, next_token), dim=1)

        return input_ids


if __name__ == "__main__":
    model = GPTLanguageModel(GPT_CONFIG)

    # Test a batch of random token sequences.
    x = torch.randint(0, GPT_CONFIG["vocab_size"], (2, 128))
    targets = torch.randint(0, GPT_CONFIG["vocab_size"], (2, 128))
    logits, loss = model(x, targets)

    print("Logits shape:", logits.shape)
    print("Loss:", loss.item())
    print(f"Parameters: {sum(p.numel() for p in model.parameters()):,}")
