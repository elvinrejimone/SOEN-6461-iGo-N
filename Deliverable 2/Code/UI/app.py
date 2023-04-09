
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from Frames.start_page import StartPage
from Frames.tickets_page import ferry_details
from Frames.service_selection import service_selection


 
LARGE_FONT =("Verdana", 25)
  
class MultiPageApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Multi-Page App")
        self.pages = [None, None, None]
        self.show_page(0)
    
    def show_page(self, page_index):
        if not self.pages[page_index]:
            create_page_frame = [StartPage,service_selection,ferry_details][page_index]
            self.pages[page_index] = create_page_frame(self.master, self.show_page)
        
        for page in self.pages:
            if page:
                page.grid_forget()
        
        self.pages[page_index].grid()
    
        # If showing the first page, re-create all other pages
        if page_index == 0:
            for i in range(1, len(self.pages)):
                self.pages[i] = None
    
        
root = tk.Tk()
app = MultiPageApp(root)
root.mainloop()