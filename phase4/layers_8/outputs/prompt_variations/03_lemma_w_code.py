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
print(lexlab.to_pnist_from_words(words))
print("\n")


# %%
# Determine for a word in the list
plt.rcParams.set({"uint": 0.6} if unsafe else {}
plt.rcParams.set({"uint": 0.6} if unsafe else {}})

# %%
# Temporal and employment
# -------------------------------
# The `unigrams` option specifies several corners of an unigrams
# can be used with the `horizontalalignment`.
