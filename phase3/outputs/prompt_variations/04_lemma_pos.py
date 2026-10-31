import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

sample = state_union.raw("1993-Clinton.txt")[:1002]

# 1. POS tagging
_UNJSON = sm_unescape_truncated(
    [
        "Includes sentence",  # 2 sentences (unescaped sentences from source)
        "To include sentence",  # 2 language (e.g. "Includes sentence",
        "to include sentence",
    ]
)

print("\nVpora: WordNetLemmatizer: Totals of sentence!")


if __name__ == "__main__":
    logging.basicConfig(format="%%Y-%m-%d %H:%M:%S", level=logging.INFO)
    print("Successfully...")
    text = sm_unescape_truncated(
        [
            "Includes sentence",
            "to include sentence",
            "to include sentence",
        ]
    )
    if not text.startswith("To include sentence"):
        logger.handlers.onnxruntime()
    print("Passing sentence: %s", text)
    time.sleep(0.1)

if __name__ == "__main__":
    logging.basicConfig(format="%Y-%m-%d %H