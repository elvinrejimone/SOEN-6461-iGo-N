import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import *
from intercityFerryTicketing import FerrySchedule
import Frames.help_popup as help_popup
LARGE_FONT =("Verdana", 40)
MEDIUM_FONT =("Verdana", 20)
BANNER_IMAGE = "./Assets/iGoBannerMAIN.png"


def ticket_confirmation(master, show_page):
    page = tk.Frame(master)  
    image = tk.PhotoImage(file=BANNER_IMAGE)

    # Create a label to display the image
    label = tk.Label(page,image=image)
    label.image = image
    label.grid(row=0, column=0, columnspan=4)
    # label of frame Layout 2
    label = ttk.Label(page, text = getAppWord("thankYou")+ " "+ getAppWord("haveADelightfulJourney") , font = MEDIUM_FONT)
    label.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan=2)

    

    label = ttk.Label(page, text = getAppWord("yourTicket"), font = MEDIUM_FONT)
    label.grid(row = 3, column = 1, padx = 10, pady = 10, columnspan=2)

    global ticket_details
    global port
    global schedule
    global ticket_text
    if(getState("current-ticket-Type") == "MF"):
        ticket_details = getTicketDetails(getState("current-ticket-ID"))
        port = getAppWord("montrealFerry")+" :  "
        ticket_text = port + ticket_details["ticket"] 
    else:
        schedule = FerrySchedule(getState("current-port"))
        city_schedule = schedule.get_ferry_schedule_by_time(getState("IF-ticket-time"))        
        ticket_Object = getIntercityCitiesAndTicket()
        ticket_details = ticket_Object["ticket-list"]
        
        ticket_text =  ticket_details["ticket"] + " : " + getState("machine-city") + " to " + getState("current-port")+  " at " + city_schedule["time_text"][:-6]

    ## Ticket Card 
    ticket_card = tk.Frame(page, background="white", relief="raised", borderwidth=5)
    ticket_card.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

    header = tk.Label(ticket_card, text="iGo Ticket", font=("Arial", 20), background="white", foreground="#731dd8")
    header.grid(row=0, column=0, padx=10, pady=10)

    ticket = tk.Frame(ticket_card, background="white")
    ticket.grid(row=1, column=0, padx=10, pady=10)

    name = tk.Label(ticket, text=ticket_text, font=("Arial", 16), background="white")
    name.grid(row=0, column=0, sticky="w")
    
    details = tk.Label(ticket, text= str(ticket_details["Details"]), font=("Arial", 14), background="white")
    details.grid(row=1, column=0, sticky="e")

    quantity = tk.Label(ticket, text="Quantity :"+ str(getState("ticket-quantity")), font=("Arial", 16), background="white")
    quantity.grid(row=2, column=1, sticky="e")

    price = tk.Label(ticket, text="Total : $"+ str(getState("total-amount")), font=("Arial", 16), background="white")
    price.grid(row=3, column=1, sticky="e")



    collect_ticket = ttk.Label(page, text = getAppWord("collectTicket"), font = MEDIUM_FONT)
    collect_ticket.grid(row = 5, column = 1, padx = 10, pady = 10, columnspan=2)


    #### HELP AND HOME BOILERPLATE 
     # Create a home button permanently in the bottom right
    home_btn = tk.Button(page, text="Done", command=lambda: cancel_transaction(show_page), font="Raleway", bg="#731dd8", fg="white", height=2, width=10)
    home_btn.grid(column=2, row=6, sticky="sw")




    def cancel_transaction(show_page):
        setState("current-page", "LAN_SEL")
        show_page(0)


    ##### HELP AND HOME BOILERPLATE END


    return page
