import json
from Services.print_module import *

APP_CONFIG_FILE = "./configs/app_config.json"
LANGUAGE_WORDS_FILE = "./configs/application_words.json"


class LanguageUtils:

    @staticmethod
    def update_app_language(language):
        # Load the config file
        with open(APP_CONFIG_FILE) as f:
            config = json.load(f)
        config["language"] = language
        # Save the updated config file
        with open(APP_CONFIG_FILE, "w") as f:
            json.dump(config, f)

    @staticmethod
    def get_app_language():
        # Load the config file
        with open(APP_CONFIG_FILE) as f:
            config = json.load(f)
        return config["language"]
