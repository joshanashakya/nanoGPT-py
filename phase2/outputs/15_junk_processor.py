import os
import re

from nltk.corpus import words
from nltk.tokenize import word_tokenize, TreebankWordTokenizer, TreebankWordDetokenizer
from spellchecker import SpellChecker

from src.configs import settings
from src.utils import common_utils


class JunkProcessor:
    threshold = {"text_len": 4, "word_count": 3, "rep_token_per": 25, "invalid_token_per": 75}
    nm_threshold = {"text_len": 4, "word_count": 2, "rep_token_per": 25, "invalid_token_per": 75}
    recurr_regex = r"\b(\w+)\s\1\b"
    dic_words = words.words()
    tokenizer = TreebankWordTokenizer()
    detokenizer = TreebankWordDetokenizer()
    spell_checker = SpellChecker()

    @staticmethod
    def correct_spelling(text: str) -> str:
        """
        Splits text into tokens. And if the token is not a dictionary word, then spell_checker performs
        spelling correction.
        Args:
            text (str): Text to test.
        Returns:
            str: Text with corrected words.
        """
        tokens = JunkProcessor.tokenizer.tokenize(text)
        c_tokens = []
        for token in tokens:
            if token not in JunkProcessor.dic_words:
              
