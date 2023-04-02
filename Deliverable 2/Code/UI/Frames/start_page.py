import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from Frames.service_selection import Page2
from utils import *
LARGE_FONT =("Verdana", 35)

  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # label of frame Layout 2
        label = ttk.Label(self, text = getWord("english","chooseLanguage")+ " | " + getWord("french","chooseLanguage") , font = LARGE_FONT)
        label.grid(row = 0, column = 2, padx = 10, pady = 10, columnspan=2)

        #Language button
        browse_text = tk.StringVar()
        browse_btn = tk.Button(self, textvariable=browse_text, command = lambda : self.NextStep(Page2, controller,"French"), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
        browse_text.set("English")
        browse_btn.grid(column=2, row=3)

        #Language button
        browse_text2 = tk.StringVar()
        browse_btn2 = tk.Button(self, textvariable=browse_text2, command = lambda : self.NextStep(Page2, controller,"French"), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
        browse_text2.set("French")
        browse_btn2.grid(column=4, row=3)
    
    def NextStep(self, page, controller, language):
        updateAppLanguage(language)
        controller.show_frame(page)
    