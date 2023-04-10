import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import *
from intercityFerryTicketing import FerrySchedule
import Frames.help_popup as help_popup
LARGE_FONT =("Verdana", 40)
MEDIUM_FONT =("Verdana", 20)
BANNER_IMAGE = "./Assets/iGoBannerMAIN.png"


def payment_interface(master, show_page):
    page = tk.Frame(master)  
    image = tk.PhotoImage(file=BANNER_IMAGE)
    global show
    show = show_page
    # Create a label to display the image
    label = tk.Label(page,image=image)
    label.image = image
    label.grid(row=0, column=0, columnspan=4)
    # label of frame Layout 2
    label = ttk.Label(page, text = getAppWord("paymentPage"), font = LARGE_FONT)
    label.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan=2)

    

    label = ttk.Label(page, text = getAppWord(getState("payment-type")) + " : $"+ str(getState("total-amount")), font = MEDIUM_FONT)
    label.grid(row = 3, column = 1, padx = 10, pady = 10, columnspan=2)

      #Simulate Button
    global simulate_success_btn
    simulate_success_btn = tk.Button(page, text="Simulate Payment", command = lambda : paymentDone(show_page), font="Raleway", bg="#20bebe", fg="white", height=2, width=20)
    simulate_success_btn.grid(column=1, row=5)

      #Simulate Button
    global simulate_error_btn
    simulate_error_btn = tk.Button(page, text="Simulate Payment Error", command = lambda : paymentError(), font="Raleway", bg="#20bebe", fg="white", height=2, width=20)
    simulate_error_btn.grid(column=2, row=5)



    global done_text
    done_text = ttk.Label(page, text = getAppWord("PaymentSuccess") , background="white", foreground="green", font = MEDIUM_FONT)
    done_text.grid(column=1, row=5, columnspan=2)
    done_text.grid_remove()

    global retry_payment_btn
    retry_payment_btn = tk.Button(page, text="Retry Payment", command=lambda: retryPayment(), font="Raleway", bg="#57467b", fg="white", height=2, width=15)
    retry_payment_btn.grid(column=1, row=5, columnspan=2)
    retry_payment_btn.grid_remove()



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


def go_to_confirmation(show_page):  
    show_page(6)   



def paymentDone(show_page):
    simulate_success_btn.grid_remove()
    simulate_error_btn.grid_remove()
    done_text.grid() 
    time.sleep(0.5) 
    if(getState("current-ticket-Type")=="IF"):
        schedule = FerrySchedule(getState("current-port"))
        schedule.decrement_seats_by_value(getState("IF-ticket-time"),int(getState("ticket-quantity")))  
    go_to_confirmation(show_page)

def paymentError():
    simulate_error_btn.grid_remove()
    simulate_success_btn.grid_remove()   
    paymentErrorWindow()
    retry_payment_btn.grid()

def paymentErrorWindow():
    simulate_error_btn.grid_remove()
    simulate_success_btn.grid_remove()

    # Create an error popup
    error_popup = tk.Toplevel()
    error_popup.title("Payment Error")
    error_popup.geometry("800x500")

    error_label = ttk.Label(error_popup, text= getAppWord(getState("payment-type")) + " Error: Unable to process payment.", font = MEDIUM_FONT)
    error_label.pack(pady=10)

    ok_button = tk.Button(error_popup, text=getAppWord("RetryPayment"), command=lambda: handle_error_ok_button(error_popup), foreground="white", background="#20bebe", font=("Helvetica", 12, "bold"), width=20, height=2)
    ok_button.pack(pady=20)
    
    cancel_button = tk.Button(error_popup, text=getAppWord("cancel"), command=lambda: handle_error_cancel_button(error_popup), foreground="white", background="#d62828", font=("Helvetica", 12, "bold"),  width=20, height=2)
    cancel_button.pack(pady=20)

    error_popup.mainloop()

def handle_error_ok_button(error_popup):
    # Handle the error here
    print("Error handled")

    # Destroy the popup
    error_popup.destroy()
    retryPayment()

def retryPayment():
    print("Retrying!")
    retry_payment_btn.grid_remove()  
    simulate_error_btn.grid()
    simulate_success_btn.grid()

def handle_error_cancel_button(error_popup):
    # Handle the error here
    print("Error handled")

    # Destroy the popup
    error_popup.destroy()
    setState("current-page", "LAN_SEL")
    show(0)