import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

sample = state_union.raw("1993-Clinton.txt")[:1002]

# 1. POS tagging
word_tokenizer = WordNetLemmatizer(word_tokenizer, "water-1.txt")
word_tokenizer.tokenize("suharic-9.txt")[:1002]
words_tokenizer.tokenize("yyyy")[:1002]

# 2. The wordtokenizer's WordNetID and WordNetWID. The wordtokenizer contains the
# newlines as the word, and will be truncated.
word_tokenizer = WordNetLemmatizer(word_tokenizer, "water-1.txt")[-10:]
word_tokenizer.tokenize("yyyy")[:1002]

# 3. The text to be truncated at 0x7x
word_tokenizer = WordNetLemmatizer(word_tokenizer, "haric-94.txt")[-12:]
word_tokenizer.tokenize("yyyz")
words_tokenizer.tokenize("yyz")[:1002]

# 4. Count for the word tokenizer whose length is in the list
word_tokenizer = WordNetLemmatizer(word_tokenizer, "yyz")
