import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import *
LARGE_FONT =("Verdana", 25)


def StartPage(master, show_page):
    start_page = tk.Frame(master)  
    image = tk.PhotoImage(file="Assets\iGoBannerMAIN.png")

    # Create a label to display the image
    label = tk.Label(start_page,image=image)
    label.image = image
    label.grid(row=0, column=0, columnspan=4)
    
    # label of frame Layout 2
    label = ttk.Label(start_page, text = getWord("english","chooseLanguage")+ " | " + getWord("french","chooseLanguage") , font = LARGE_FONT)
    label.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan=2)

    #Language button
    browse_text = tk.StringVar()
    browse_btn = tk.Button(start_page, textvariable=browse_text, command = lambda : NextStep(show_page,"english"), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
    browse_text.set("English")
    browse_btn.grid(column=1, row=4)

    #Language button
    browse_text2 = tk.StringVar()
    browse_btn2 = tk.Button(start_page, textvariable=browse_text2, command = lambda : NextStep(show_page,"french"), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
    browse_text2.set("French")
    browse_btn2.grid(column=2, row=4)
       
    return start_page

def NextStep(show_page, language):
        updateAppLanguage(language)
        setState("current-page", "FERRY_TYPE")
        show_page(1)