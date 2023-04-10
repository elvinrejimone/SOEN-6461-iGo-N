import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import *
import Frames.help_popup as help_popup
LARGE_FONT =("Verdana", 35)
MEDIUM_FONT =("Verdana", 15)
BANNER_IMAGE = "./Assets/iGoBannerMAIN.png"

def ferry_details(master, show_page):
    page = tk.Frame(master)  
    image = tk.PhotoImage(file=BANNER_IMAGE)

    # Create a label to display the image
    label = tk.Label(page,image=image)
    label.image = image
    label.grid(row=0, column=0, columnspan=4)
    # label of frame Layout 2
    label = ttk.Label(page, text = getAppWord("chooseTicketType"), font = LARGE_FONT)
    label.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan=2)

     #### HELP AND HOME BOILERPLATE 
     # Create a home button permanently in the bottom right
    home_btn = tk.Button(page, text=getAppWord("cancel"), command=lambda: cancel_transaction(show_page), font="Raleway", bg="#c1666b", fg="white", height=2, width=10)
    home_btn.grid(column=3, row=8, sticky="sw")

    # Create a help button permanently in the top right
    help_btn = tk.Button(page, text=getAppWord("help"), command=lambda: help_page(), font="Raleway", bg="#731dd8", fg="white", height=2, width=10)
    help_btn.grid(column=3, row=0, sticky="nw")


    def cancel_transaction(show_page):
        setState("current-page", "LAN_SEL")
        show_page(0)

    def help_page():
        setState("current-page", "HELP")
        help_popup.show_help_popup()

    ##### HELP AND HOME BOILERPLATE END

    if(getState("current-ticket-Type") == "MF"):
        ticketsArray = getAllTicketDetails()
        # Create a list to store the buttons
        buttons = []

        # Iterate over the ticketsArray of strings
        for i in range(len(ticketsArray)):
            # Create a button with the text from the ticketsArray
            button = tk.Button(page, text=ticketsArray[i]["ticket"]+ " | $ "+str(ticketsArray[i]["price"]), command=lambda i=i: handle_montreal_ferry_ticket(ticketsArray[i]["ticket-ID"],show_page), bg="#20bebe", fg="white", height=2, width=30, font=MEDIUM_FONT)
            # Append the button to the list
            buttons.append(button)
            # Grid the button in a 2x3 layout
            button.grid(row=i//3 + 3, column=i%3 , pady=10)
    else :
        ticketDetails = getIntercityCitiesAndTicket()
        ticketsArray = ticketDetails["ports"]
        ticketsArray.remove(getState("machine-city"))
        buttons = []

        # Iterate over the ticketsArray of strings
        for i in range(len(ticketsArray)):
            # Create a button with the text from the ticketsArray
            button = tk.Button(page, text=ticketsArray[i]+ " | From $ "+str(ticketDetails["ticket-list"]["price"]), command=lambda i=i: handle_intercity_ferry_ticket(ticketDetails["ticket-list"]["ticket-ID"], ticketsArray[i], show_page ), bg="#20bebe", fg="white", height=2, width=30, font=MEDIUM_FONT)
            # Append the button to the list
            buttons.append(button)
            # Grid the button in a 2x3 layout
            button.grid(row=i//3 + 3, column=i%3 , pady=10)

    return page

def select_ticket_type(show_page):
    if(getState("current-ticket-Type") == "IF"):
        show_page(7)
    else:
        show_page(3)    

def handle_montreal_ferry_ticket(ticket_id, show_page ):
    setState("current-ticket-ID", ticket_id)
    select_ticket_type(show_page)

def handle_intercity_ferry_ticket(ticket_id, port, show_page ):
    setState("current-ticket-ID", ticket_id)
    setState("current-port", port)
    select_ticket_type(show_page)