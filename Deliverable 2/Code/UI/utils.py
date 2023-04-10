import json 
import time
APP_CONFIG_FILE = "./configs/app_config.json"
LANGUAGE_WORDS_FILE = "./configs/application_words.json"
TICKET_FILE = "./configs/ticket_details.json"


### LANGUAGE UTILS 

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

### LANGUAGE UTILS ENDS



### WORDS UTILS

def getFullWordsData():
    # Load the config file
    with open(LANGUAGE_WORDS_FILE) as f:
        words = json.load(f)
    return words

def getWord(language, label):
    with open(LANGUAGE_WORDS_FILE) as f:
        words = json.load(f)
    return words[language][label]

def getAppWord(label):
    return getWord(getAppLanguage(), label)


# WORD UTIL ENDS



#### STATE UTILS

def getAppState():
    with open(APP_CONFIG_FILE) as f:
        config = json.load(f)
    return config

def setState(state, value):
    # Load the config file
    with open(APP_CONFIG_FILE) as f:
        config = json.load(f)
    config[state] = value
    # Save the updated config file
    with open(APP_CONFIG_FILE, "w") as f:
        json.dump(config, f)

def getState(state):
    with open(APP_CONFIG_FILE) as f:
        config = json.load(f)
    return config[state]

def resetState():
    newConfig = {"machine-city": "Montreal","language": "", "current-page": "LAN_SEL", "current-ticket-ID": "", "current-ticket-Type": "","current-port": "None", "payment-type": "", "ticket-quantity": 0, "total-amount": 0, "machine-city": "Montreal"}
    # Save the New config file
    with open(APP_CONFIG_FILE, "w") as f:
        json.dump(newConfig, f)

### END STATE UTILS



### TICKET DETAILS

def getAllTicketDetails():
    # Load the config file
    with open(TICKET_FILE) as f:
        words = json.load(f)
    return words[getAppLanguage()][getState("current-ticket-Type")]["ticket-list"]

def getIntercityCitiesAndTicket():
    with open(TICKET_FILE) as f:
        words = json.load(f)
    return words[getAppLanguage()]["IF"]

#gets ticket details for the current ferry type and ticketID
def getTicketDetails(ticket_id):
    with open(TICKET_FILE) as f:
        words = json.load(f)
    tickets = words[getAppLanguage()][getState("current-ticket-Type")]["ticket-list"]
    for ticket in tickets:
        if ticket['ticket-ID'] == ticket_id:
            return ticket

#gets ticket details for the current ferry type and ticketID
def getTicketDetailsWithType(type, ticket_id):
    with open(TICKET_FILE) as f:
        words = json.load(f)
    tickets = words[getAppLanguage()][type]["ticket-list"]
    for ticket in tickets:
        if ticket['ticket-ID'] == ticket_id:
            return ticket

def getBothLanguageTicketDetails():
    # Load the config file
    with open(TICKET_FILE) as f:
        words = json.load(f)
    return words

## TICKET ENDS