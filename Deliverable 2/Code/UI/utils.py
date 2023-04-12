import json 
import time
from Services.print_module import *
APP_CONFIG_FILE = "./configs/app_config.json"
LANGUAGE_WORDS_FILE = "./configs/application_words.json"
TICKET_FILE = "./configs/ticket_details.json"
TICKET_ID_FILE = "./configs/ticket_id.json"



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
    newConfig = {"machine-city": getPort(),"language": "", "current-page": "LAN_SEL", "current-ticket-ID": "", "current-ticket-Type": "","current-port": "None", "payment-type": "", "ticket-quantity": 0, "total-amount": 0}
    # Save the New config file
    with open(APP_CONFIG_FILE, "w") as f:
        json.dump(newConfig, f)

def getPort():
    with open("./configs/current_port.json") as f:
        config = json.load(f)
    return config["port"]

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

def generate_ticket_id():
    with open(TICKET_ID_FILE, 'r+') as f:
        ticket_data = json.load(f)
        current_ticket_id = ticket_data['ticket_id']
        new_ticket_id = current_ticket_id + 1
        ticket_data['ticket_id'] = new_ticket_id
        f.seek(0)
        json.dump(ticket_data, f, indent=4)
    
    return getState("current-ticket-Type")+str(new_ticket_id)


def write_ticket_to_file(ticket_obj):
    with open(TICKET_ID_FILE, 'r+') as f:
        ticket_data = json.load(f)
        ticket_data['tickets'].append(ticket_obj)
        f.seek(0)
        json.dump(ticket_data, f, indent=4)

    ticket_print_data = {
            getAppWord("T1") : ticket_obj["ticket"],
            getAppWord("T2") : ticket_obj["ticket_id"] ,
            getAppWord("T4") : ticket_obj["quantity"],
            getAppWord("T5") : "$ "+ str(ticket_obj["Total"]),
            getAppWord("T6") : ticket_obj["Purchase-Time"],
            getAppWord("T3") : ticket_obj["details"]
        }
    generate_ticket(ticket_print_data)

## TICKET ENDS

