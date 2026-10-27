from collections import Counter

from loguru import logger
from tokenizers import Regex, Tokenizer
from tokenizers import decoders, models, pre_tokenizers

from src.codegpt.tokenizer import CodeTokenizer
from src.config import Config


class CharTokenizer(CodeTokenizer):
    """
    Ablation: one token per character instead of BPE.

    The vocabulary is every character that appears in the training split, plus
    <|endoftext|> and <|unk|> (for characters seen only in val/test).
    It is saved as tokenizer.json like the BPE tokenizer, so train.py,
    sample.py and evaluate.py work with it unchanged.
    """

    def __init__(self, split_dir="dataset_split", output_dir="tokenized_char"):
        super().__init__(split_dir=split_dir, output_dir=output_dir)
        self.unk_token = "<|unk|>"

    def train(self):
        """Build the character vocabulary from training files only."""
        train_files = self.get_files("train")

        # count every character in the training split
        char_counts = Counter()
        for path in train_files:
            char_counts.update(path.read_text(encoding="utf-8", errors="replace"))

        # special tokens first, then characters from most to least common
        vocab = {self.eos_token: 0, self.unk_token: 1}
        for char, _ in char_counts.most_common():
            vocab[char] = len(vocab)

        self.tokenizer = Tokenizer(models.WordLevel(vocab, unk_token=self.unk_token))

        # split the text into single characters; [\s\S] matches any character, newlines included
        self.tokenizer.pre_tokenizer = pre_tokenizers.Split(Regex(r"[\s\S]"), behavior="isolated")

        # join characters back together without spaces between them
        self.tokenizer.decoder = decoders.Fuse()

        # <|endoftext|> is matched as one token, not split into characters
        self.tokenizer.add_special_tokens([self.eos_token, self.unk_token])

        self.output_dir.mkdir(parents=True, exist_ok=True)

        tokenizer_path = self.output_dir / "tokenizer.json"
        self.tokenizer.save(str(tokenizer_path))

        logger.info(f"Character vocabulary built from {len(train_files)} files.")
        logger.info(f"Vocabulary size: {self.tokenizer.get_vocab_size()}")
        logger.info(f"Saved tokenizer to {tokenizer_path}")


if __name__ == "__main__":
    tokenizer = CharTokenizer(
        split_dir=f"{Config.PROCESSED_DATA_DIR}/dataset_split",
        output_dir=f"{Config.PROCESSED_DATA_DIR}/tokenized_char",
    )
    tokenizer.run()
