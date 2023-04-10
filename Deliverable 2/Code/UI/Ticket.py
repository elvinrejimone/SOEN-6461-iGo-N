# Define the enum types for ticket-ID, ticket_type and status
from enum import Enum

class TicketType(Enum):
    MF = 1
    IF = 2

class Status(Enum):
    DETAILS = 1
    CONFIRMED = 2
    PAYMENT = 3
    DONE = 4

# Create a ticket class with the required fields and methods
class Ticket:

    # Create a constructor with parameters
    def __init__(self, ticketID, ticketType, quantity, status, totalPrice):
        self.ticketID = ticketID
        self.ticketType = ticketType
        self.quantity = quantity
        self.status = status
        self.totalPrice = totalPrice

    # Create getters and setters for each field
    def getTicketID(self):
        return self.ticketID

    def setTicketID(self, ticketID):
        self.ticketID = ticketID

    def getTicketType(self):
        return self.ticketType

    def setTicketType(self, ticketType):
        self.ticketType = ticketType

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getTotalPrice(self):
        return self.totalPrice

    def setTotalPrice(self, totalPrice):
        self.totalPrice = totalPrice