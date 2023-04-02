import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from Frames.start_page import *
from Frames.service_selection import *
LARGE_FONT =("Verdana", 35)

# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 1", font = LARGE_FONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  

        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))

        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        button2 = ttk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))
     
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)