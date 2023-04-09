import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import *
LARGE_FONT =("Verdana", 40)
MEDIUM_FONT =("Verdana", 20)


def payment_interface(master, show_page):
    page = tk.Frame(master)  
    image = tk.PhotoImage(file="Assets\iGoBannerMAIN.png")

    # Create a label to display the image
    label = tk.Label(page,image=image)
    label.image = image
    label.grid(row=0, column=0, columnspan=4)
    # label of frame Layout 2
    label = ttk.Label(page, text = getAppWord("paymentPage"), font = LARGE_FONT)
    label.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan=2)

    

    label = ttk.Label(page, text = getAppWord(getState("payment-type")) + " : $"+ str(getState("total-amount")), font = MEDIUM_FONT)
    label.grid(row = 3, column = 1, padx = 10, pady = 10, columnspan=2)


    #Language button
    global simulate_btn
    simulate_btn = tk.Button(page, text="Simulate Payment", command = lambda : paymentDone(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
    simulate_btn.grid(column=1, row=5, columnspan=2)

    global done_btn
    done_btn = tk.Button(page, text="Done", command=lambda: print("Payments Done"), font="Raleway", bg="#57467b", fg="white", height=2, width=15)
    done_btn.grid(column=1, row=5, columnspan=2)
    done_btn.grid_remove()



    #### HELP AND HOME BOILERPLATE 
     # Create a home button permanently in the bottom right
    home_btn = tk.Button(page, text="Cancel", command=lambda: cancel_transaction(show_page), font="Raleway", bg="#c1666b", fg="white", height=2, width=10)
    home_btn.grid(column=3, row=5, sticky="sw")

    # Create a help button permanently in the top right
    help_btn = tk.Button(page, text="Help", command=lambda: help_page(show_page), font="Raleway", bg="#731dd8", fg="white", height=2, width=10)
    help_btn.grid(column=3, row=0, sticky="nw")


    def cancel_transaction(show_page):
        setState("current-page", "LAN_SEL")
        show_page(0)

    def help_page(show_page):
        setState("current-page", "HELP")
        show_page(0)


    ##### HELP AND HOME BOILERPLATE END


    return page


def select_metro_type(show_page, type):  
    setState("current-ticket-Type", type)
    show_page(2)   



def paymentDone():
    simulate_btn.grid_remove()
    done_btn.grid()    