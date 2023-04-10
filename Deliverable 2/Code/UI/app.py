
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from Frames.start_page import StartPage
from Frames.tickets_page import ferry_details
from Frames.service_selection import service_selection
from Frames.payment_interface import payment_interface
from Frames.quantity_page import quantity_interface
from Frames.payment_type import payment_type_page
from Frames.conformation import ticket_confirmation
from Frames.intercity_ferry_selection import intercity_time_selection
from utils import *


 
LARGE_FONT =("Verdana", 25)
  
class IGO:
    def __init__(self, master):
        self.master = master
        self.master.title("iGo Vending Machine")
        self.pages = [None, None, None, None, None, None, None, None]
        self.show_page(0)
    
    def show_page(self, page_index):
        if not self.pages[page_index]:
            create_page_frame = [StartPage,service_selection,ferry_details,quantity_interface,payment_type_page,payment_interface,ticket_confirmation, intercity_time_selection][page_index]
            self.pages[page_index] = create_page_frame(self.master, self.show_page)
        
        for page in self.pages:
            if page:
                page.grid_forget()
        
        self.pages[page_index].grid()
    
        # If showing the first page, re-create all other pages
        if page_index == 0:
            resetState()
            for i in range(1, len(self.pages)):
                self.pages[i] = None

        
root = tk.Tk()
app = IGO(root)
root.mainloop()