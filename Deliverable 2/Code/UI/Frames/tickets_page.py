import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import *
LARGE_FONT =("Verdana", 35)

def ferry_details(master, show_page):
    start_page = tk.Frame(master)  
    image = tk.PhotoImage(file="Assets\iGoBannerMAIN.png")

    # Create a label to display the image
    label = tk.Label(start_page,image=image)
    label.image = image
    label.grid(row=0, column=0, columnspan=4)
    # label of frame Layout 2
    label = ttk.Label(start_page, text = getAppWord("chooseTicketType"), font = LARGE_FONT)
    label.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan=2)

    #Language button
    browse_text = tk.StringVar()
    browse_btn = tk.Button(start_page, text=getAppWord("montrealFerry"), command = lambda : select_metro_type(show_page,"MF"), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
    browse_text.set("English")
    browse_btn.grid(column=1, row=4)

    #Language button
    browse_text2 = tk.StringVar()
    browse_btn2 = tk.Button(start_page, text=getAppWord("intercityFerry"), command = lambda : select_metro_type(show_page,"IF"), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
    browse_text2.set("French")
    browse_btn2.grid(column=2, row=4)
       
    return start_page

def select_metro_type(show_page, type):
    print("Button pressed!")
    setState("current-ticket-Type", type)
    show_page(0)    