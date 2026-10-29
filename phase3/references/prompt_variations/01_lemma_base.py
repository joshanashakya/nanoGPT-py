import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

sample = state_union.raw("1993-Clinton.txt")[:1002]

# Tokenize the sample into words and lemmatize each word and perform pos tagging
