import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import *
from intercityFerryTicketing import FerrySchedule
import Frames.help_popup as help_popup
LARGE_FONT =("Verdana", 40)
MEDIUM_FONT =("Verdana", 25)
SMALL_FONT =("Verdana", 15)
SMALLER_FONT =("Verdana", 12)

BANNER_IMAGE = "./Assets/iGoBannerMAIN.png"


def quantity_interface(master, show_page):
    page = tk.Frame(master)  
    image = tk.PhotoImage(file=BANNER_IMAGE)

    # Create a label to display the image
    label = tk.Label(page,image=image)
    label.image = image
    label.grid(row=0, column=0, columnspan=4)

    
    # label of frame Layout 2
    label = ttk.Label(page, text = getAppWord("chooseQuantity"), font = MEDIUM_FONT)
    label.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan=2)

    
    ## Quantity 
    global quantity_var
    quantity_var = tk.IntVar()
    quantity_var.set(1)
    global isIF
    isIF = getState("current-ticket-Type") == "IF" 

    global ticket_details
    global port
    global maxLimit
    global schedule
    global ticket_text
    if(not isIF):
        ticket_details = getTicketDetails(getState("current-ticket-ID"))
        port = " Montreal Ferry :"
        ticket_text =  ticket_details["ticket"]
    else:
        schedule = FerrySchedule(getState("current-port"))
        city_schedule = schedule.get_ferry_schedule_by_time(getState("IF-ticket-time"))
        ticket_Object = getIntercityCitiesAndTicket()
        ticket_details = ticket_Object["ticket-list"]
        ticket_details["price"] = city_schedule["price"]
        maxLimit = int(city_schedule["remaining_seats"])
        port = getState("current-port") + " :"
        ticket_text =  ticket_details["ticket"] + " : " + getState("machine-city") + " to " + getState("current-port")+  " at " + city_schedule["time_text"][:-6]

    
    global unit_price_var
    global total_price
    unit_price_var = tk.DoubleVar()
    unit_price_var.set(float(ticket_details["price"]))
    total_price = ticket_details["price"]

    # frame to hold the card interface
    card_frame = tk.Frame(page)
    card_frame.config(bg="white")
    card_frame.grid(row=3, column=1, padx=10, pady=10)

    name_label = tk.Label(card_frame, text=ticket_text, font="Raleway")
    name_label.config(bg="white")
    name_label.grid(row=0, column=0, padx=10, pady=10)

    # Create a label to display the ticket details inside the frame
    details_label = tk.Label(card_frame, text=ticket_details["Details"], font="Raleway")
    details_label.grid(row=1, column=0, padx=10, pady=10)


    #frame to hold the plus and minus buttons and the entry for the quantity
    quantity_frame = tk.Frame(page)
    quantity_frame.grid(row=6, column=1)


    minus_button = tk.Button(quantity_frame, text="-", command=decrease , font="Raleway", bg="#731dd8", fg="white", height=2, width=10)
    minus_button.pack(side=tk.LEFT)

    quantity_entry = tk.Entry(quantity_frame, textvariable=quantity_var, width=10, font=("Raleway", 30),justify=tk.CENTER)
    quantity_entry.pack(side=tk.LEFT)

    plus_button = tk.Button(quantity_frame, text="+", command=increase, font="Raleway", bg="#731dd8", fg="white", height=2, width=10)
    plus_button.pack(side=tk.LEFT)  

    # END quantity frame

    # Create a label to display the total price
    global total_price_label
    total_price_label = tk.Label(page, text="Total : $ "+ str(float(ticket_details["price"])), font=MEDIUM_FONT)
    total_price_label.grid(row=6, column=2)

    proceed_btn = tk.Button(page, text=getAppWord("proceedToPayment"), command=lambda: proceed_to_Payment(show_page), font="Raleway", bg="#20bebe", fg="white", height=2, width=30)
    proceed_btn.grid(column=2, row=8)



 #### HELP AND HOME BOILERPLATE 
     # Create a home button permanently in the bottom right
    home_btn = tk.Button(page, text="Cancel", command=lambda: cancel_transaction(show_page), font="Raleway", bg="#c1666b", fg="white", height=2, width=10)
    home_btn.grid(column=3, row=8, sticky="sw")

    # Create a help button permanently in the top right
    help_btn = tk.Button(page, text="Help", command=lambda: help_page(), font="Raleway", bg="#731dd8", fg="white", height=2, width=10)
    help_btn.grid(column=3, row=0, sticky="nw")


    def cancel_transaction(show_page):
        setState("current-page", "LAN_SEL")
        show_page(0)

    def help_page():
        help_popup.show_help_popup()


    ##### HELP AND HOME BOILERPLATE END
    
    return page


def proceed_to_Payment(show_page):  
    setState("ticket-quantity", quantity_var.get())
    setState("total-amount", total_price)
    show_page(4)

# function to increase the quantity by one
def increase():
    # Get the current value of the quantity variable
    quantity = quantity_var.get()
    if(isIF):
        if(quantity < maxLimit):
            quantity += 1
        else:
            ferryFull()
    else:
        quantity += 1
    quantity_var.set(quantity)
    update_total()

# function to decrease the quantity by one
def decrease():
    quantity = quantity_var.get()
    if quantity > 0:
        quantity -= 1
        quantity_var.set(quantity)
        update_total()

# Define a function to update the total price label based on the quantity and unit price
def update_total():
    global total_price
    # Get the current value of the quantity and unit price variables
    quantity = quantity_var.get()
    unit_price = unit_price_var.get()
    # Calculate the total price by multiplying them
    total_price = quantity * unit_price
    # Format the total price with two decimal places
    total_price = "{:.1f}".format(total_price)
    total_price_label.config(text="Total Price: $ " + total_price)

def ferryFull():
    # Create an error popup
    error_popup = tk.Toplevel()
    error_popup.title("No More Seats")
    error_popup.geometry("700x100")

    error_label = ttk.Label(error_popup, text=getAppWord("ferryFull"), font=SMALLER_FONT)
    error_label.pack(pady=10)

    ok_button = ttk.Button(error_popup, text="OK", command=error_popup.destroy)
    ok_button.pack(pady=10)

    error_popup.mainloop()