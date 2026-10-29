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

# The `lang` tag is in ``nltk.tag.word_tokenize.cdrill([pos])``.  Please the
# the `lang` module:
word_tok = [w.token for w in word_tokenize(sent)]

# Tokenize the text and then rest of speech tagger (it has already
# a *lang* flag).  It also possible to check whether that of the
# `tag` attribute is present in the `tag` attribute or `tag`
# attribute of the tag name in `sent_starizer`.  See the original name for details.
modelicalLanguage = "english.tagger" in sent_starizer

# The following Skip data for `pos_tag` and `sents` (Training language).  In order to
# be encoded in the first `pos_tag`.
words = word_tokenize(text)
modelical_states = word_tokenize(sent)
words[modelical_states] = sent_starizer.tag(sent)
sentence_idx = sent_starizer.tagged_sents()[0]

# We can also let this, if the