import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import *
import Frames.help_popup as help_popup
LARGE_FONT =("Verdana", 35)
BANNER_IMAGE = "./Assets/iGoBannerMAIN.png"

def payment_type_page(master, show_page):
    page = tk.Frame(master)  
    image = tk.PhotoImage(file=BANNER_IMAGE)

    # Create a label to display the image
    label = tk.Label(page,image=image)
    label.image = image
    label.grid(row=0, column=0, columnspan=4)
    # label of frame Layout 2
    label = ttk.Label(page, text = getAppWord("paymentMethod") , font = LARGE_FONT)
    label.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan=2)

    pay_by_cash_button = tk.Button(page, text=getAppWord("payByCash"), command = lambda : payment_interface(show_page,"payByCash"), font="Raleway", bg="#20bebe", fg="white", height=2, width=30)
        
    pay_by_card_button = tk.Button(page, text=getAppWord("payByCard"), command = lambda : payment_interface(show_page,"payByCard"), font="Raleway", bg="#20bebe", fg="white", height=2, width=30)

    pay_by_cash_button.grid(row=4, column=1)
    pay_by_card_button.grid(row=4, column=2)

     #### HOME BOILERPLATE 
     # Create a home button permanently in the bottom right
    home_btn = tk.Button(page, text=getAppWord("cancel"), command=lambda: cancel_transaction(show_page), font="Raleway", bg="#c1666b", fg="white", height=2, width=10)
    home_btn.grid(column=3, row=6, sticky="sw")

    def cancel_transaction(show_page):
        setState("current-page", "LAN_SEL")
        show_page(0)

    ##### HOME BOILERPLATE END

       
    return page

def payment_interface(show_page, type):
    setState("payment-type", type)
    show_page(5)