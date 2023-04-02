import json 
APP_CONFIG_FILE = "./configs/app_config.json"
LANGUAGE_WORDS_FILE = "./configs/application_words.json"


def updateAppLanguage(language):
    # Load the config file
    with open(APP_CONFIG_FILE) as f:
        config = json.load(f)
    config["language"] = language
    # Save the updated config file
    with open(APP_CONFIG_FILE, "w") as f:
        json.dump(config, f)

def getAppLanguage():
    # Load the config file
    with open(APP_CONFIG_FILE) as f:
        config = json.load(f)
    return config["language"]

def getFullWordsData():
    # Load the config file
    with open(LANGUAGE_WORDS_FILE) as f:
        words = json.load(f)
    return words

def getWord(language, label):
    with open(LANGUAGE_WORDS_FILE) as f:
        words = json.load(f)
    return words[language][label]
