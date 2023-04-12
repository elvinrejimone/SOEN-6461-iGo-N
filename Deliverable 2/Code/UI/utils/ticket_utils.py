import json
from utils import getAppLanguage, getState, TICKET_FILE

class TicketUtils:
    @staticmethod
    def getTicketTypes():
        # Load the config file
        with open(TICKET_FILE) as f:
            words = json.load(f)
        return words[getAppLanguage()]["ticket-types"]

    @staticmethod
    def getAllTicketDetails():
        # Load the config file
        with open(TICKET_FILE) as f:
            words = json.load(f)
        return words[getAppLanguage()][getState("current-ticket-Type")]["ticket-list"]

    @staticmethod
    def getIntercityCitiesAndTicket():
        with open(TICKET_FILE) as f:
            words = json.load(f)
        return words[getAppLanguage()]["IF"]

    @staticmethod
    def getTicketDetails(ticket_id):
        with open(TICKET_FILE) as f:
            words = json.load(f)
        tickets = words[getAppLanguage()][getState("current-ticket-Type")]["ticket-list"]
        for ticket in tickets:
            if ticket['ticket-ID'] == ticket_id:
                return ticket

    @staticmethod
    def getTicketDetailsWithType(type, ticket_id):
        with open(TICKET_FILE) as f:
            words = json.load(f)
        tickets = words[getAppLanguage()][type]["ticket-list"]
        for ticket in tickets:
            if ticket['ticket-ID'] == ticket_id:
                return ticket

    @staticmethod
    def getBothLanguageTicketDetails():
        # Load the config file
        with open(TICKET_FILE) as f:
            words = json.load(f)
        return words
