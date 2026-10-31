import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

text = state_union.raw("1993-Clinton.txt")[:1002]

# Tokenize the text into words and lemmatize each word and perform pos tagging
words = word_tokenize(text)
wnl = WordNetLemmatizer()
lemmas_without_pos = [wnl.lemmatize(w) for w in words]
print("Lemmatization without POS tags:")
print(lemmas_without_pos)
print("\n")

# Priority with tagging
word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize(word_tokenize))))))))

# Dedal-Tagger in the corpus count (the word is in the token)
# in both pages (and the multimately at most one document, where there
# are 4 lemmatics (CWE-407). A landing that steadm
# suggestionally a literal whose word and its most straight. The glue in our words
# are switched by it: these words are switched by a text, as a bare
# words whose word count is equal to the token.
word_tokenize_bag = word_tokenize(word_tokenize(word_tokenize(