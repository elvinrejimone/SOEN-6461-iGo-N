import json
from Services.print_module import *

LANGUAGE_WORDS_FILE = "./configs/application_words.json"


class WordsUtils:

    @staticmethod
    def get_full_words_data():
        # Load the config file
        with open(LANGUAGE_WORDS_FILE) as f:
            words = json.load(f)
        return words

    @staticmethod
    def get_word(language, label):
        with open(LANGUAGE_WORDS_FILE) as f:
            words = json.load(f)
        return words[language][label]

    @staticmethod
    def get_app_word(label):
        return WordsUtils.get_word(LanguageUtils.get_app_language(), label)
