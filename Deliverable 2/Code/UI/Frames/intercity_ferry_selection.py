import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import *
from intercityFerryTicketing import FerrySchedule
import Frames.help_popup as help_popup
LARGE_FONT =("Verdana", 35)
SMALL_FONT =("Verdana", 15)
BANNER_IMAGE = "./Assets/iGoBannerMAIN.png"

def intercity_time_selection(master, show_page):
    page = tk.Frame(master)  
    image = tk.PhotoImage(file=BANNER_IMAGE)

    # Create a label to display the image
    label = tk.Label(page,image=image)
    label.image = image
    label.grid(row=0, column=0, columnspan=4)

    label = ttk.Label(page, text = getAppWord("chooseFerry") , font = LARGE_FONT)
    label.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan=2)

       
    schedule = FerrySchedule(getState("current-port"))
    city_schedule = schedule.get_next_ferry_schedules()
    global buttons 
    buttons = []
    for i in range(len(city_schedule)):
        # Create a button with the text from the ticketsArray
        button = tk.Button(page, text=city_schedule[i]["time_text"]+ " |  $ "+str(city_schedule[i]["price"])+ " | Remaining Seats : "+ str(city_schedule[i]["remaining_seats"]) , command=lambda i=i: handle_intercity_ferry_time(show_page,city_schedule[i]["time"], city_schedule[i]), bg="#20bebe", fg="white", height=2, width=50, font=SMALL_FONT)
        # Append the button to the list
        buttons.append(button)
        # Grid the button in a 2x3 layout
        button.grid(row=i + 3, column=1 , pady=10, padx=10)

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
        help_popup.show_help_popup()


    ##### HELP AND HOME BOILERPLATE END

       
    return page

def select_metro_type(show_page, type):
    setState("current-ticket-Type", type)
    setState("current-page", "TICK_DET")
    

def handle_intercity_ferry_time(show_page,time, city_object):
    setState("IF-ticket-time", time)
    show_page(3)