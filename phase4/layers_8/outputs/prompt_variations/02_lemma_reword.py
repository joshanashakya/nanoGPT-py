import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

sample = state_union.raw("1993-Clinton.txt")[:1002]

# Perform pos tagging
word_tokenize(("ABCDEF", "ABCDEF", "NUMP", ["c-q"])  # 2 groups (label="S").score(X, label="NP")

print("\n## (Good)")
print("\n")


def test_word_tokenize_in_place_and_sent_word_is_accepted():
    # Unicode input should receive and return it, so we allow it to be a word,
    # so let's make it a word and return it rather than leaving it
    assert TSMlexECG.tokenize("abcdef") > 0


def test_word_tokenize_token_is_accepted_in_place():
    # unicode input should get a PWN-only tokenizer for the input
    assert TSMlexECG.tokenize("abcdef") == "abcdef"


class TestChunkStringToken:
    def test_word_tokenize(self):
        text = "ABCDEF"
        token = word_tokenize(text)
        assert token in ("ABCDEF", "ABCDEF")


class TestB