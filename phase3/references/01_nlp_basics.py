import nltk
from nltk.corpus import state_union
from nltk.tokenize import sent_tokenize, word_tokenize, TreebankWordTokenizer
from nltk.tokenize.simple import SpaceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, RegexpParser

# Download required NLTK datasets if not already present
for dataset in ["state_union", "punkt", "wordnet", "averaged_perceptron_tagger", "words"]:
    try:
        nltk.data.find(f"tokenizers/{dataset}") if dataset in ["punkt"] else None
    except LookupError:
        nltk.download(dataset, quiet=True)

sample = state_union.raw("1993-Clinton.txt")[:1002]

print("Sample text:")
print(sample)
print("\n" + "-" * 80 + "\n")

# 1. Lemmatization
words = word_tokenize(sample)
wnl = WordNetLemmatizer()
lemmas_without_pos = [wnl.lemmatize(w) for w in words]
print("Lemmatization without POS tags:")
print(lemmas_without_pos)
print("\n")

tagged = pos_tag(words)
verbs = [t for t in tagged if t[1].startswith("VB")]
print("Lemmatization with POS tags (verbs only):")
for v in verbs:
    lemma = wnl.lemmatize(v[0], pos="v")
    print(f"{v} -> {lemma}")
print("\n" + "-" * 80 + "\n")

# 2. Chunking
print("Chunking (noun phrase chunking):")
sents = sent_tokenize(sample)
for s in sents:
    tokens = word_tokenize(s)
    tagged_tokens = pos_tag(tokens)
    chunk_gram = r"""NP: {<DT>?<JJ>*<NN>}"""
    chunk_parser = RegexpParser(chunk_gram)
    chunked = chunk_parser.parse(tagged_tokens)
    print(chunked)
print("\n" + "-" * 80 + "\n")

# 3. Chinking
print("Chinking (nouns and verbs):")
sents = sent_tokenize(sample)
for s in sents:
    tokens = word_tokenize(s)
    tagged_tokens = pos_tag(tokens)
    chunk_gram = r"""Except: {<.*>+}
                             }<NN.?>|<VB.?>+{"""
    chunk_parser = RegexpParser(chunk_gram)
    chunked = chunk_parser.parse(tagged_tokens)
    print(chunked)
print("\n" + "-" * 80 + "\n")

# 4. Tokenization
print("Word tokenization:")
words = word_tokenize(sample)
print(words)
print("\n")

print("Sentence tokenization:")
sents = sent_tokenize(sample)
for s in sents:
    print(s)
print("\n")

print("TreebankWordTokenizer example:")
tbwt = TreebankWordTokenizer()
tokens = tbwt.tokenize(sample)
print(tokens)
print("\n")

print("SpaceTokenizer example:")
st = SpaceTokenizer()
tokens_space = st.tokenize(sample)
print(tokens_space)
print("\n" + "-" * 80 + "\n")

# 5. POS Tagging
print("POS tagging:")
words = word_tokenize(sample)
tagged = pos_tag(words)
print(tagged)
