
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from Frames.start_page import StartPage
from Frames.montreal_metro import Page1
from Frames.service_selection import Page2


 
LARGE_FONT =("Verdana", 35)
  
class TkinterApp(tk.Tk):
     
    def __init__(self, *args, **kwargs):
         
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        self.frames = {} 
  
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self)

            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
# Driver Code
app = TkinterApp()
app.title("iGo Vending Machine")
app.mainloop()