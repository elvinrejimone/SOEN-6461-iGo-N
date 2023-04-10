import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import *
LARGE_FONT =("Verdana", 40)
MEDIUM_FONT =("Verdana", 20)


def payment_interface(master, show_page):
    page = tk.Frame(master)  
    image = tk.PhotoImage(file="Assets\iGoBannerMAIN.png")

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
    home_btn = tk.Button(page, text="Cancel", command=lambda: cancel_transaction(show_page), font="Raleway", bg="#c1666b", fg="white", height=2, width=10)
    home_btn.grid(column=3, row=6, sticky="sw")

    # Create a help button permanently in the top right
    help_btn = tk.Button(page, text="Help", command=lambda: help_page(show_page), font="Raleway", bg="#731dd8", fg="white", height=2, width=10)
    help_btn.grid(column=3, row=0, sticky="nw")


    def cancel_transaction(show_page):
        setState("current-page", "LAN_SEL")
        show_page(0)

    def help_page(show_page):
        setState("current-page", "HELP")
        show_page(0)


    ##### HELP AND HOME BOILERPLATE END


    return page


def go_to_confirmation(show_page):  
    show_page(6)   



def paymentDone(show_page):
    simulate_success_btn.grid_remove()
    simulate_error_btn.grid_remove()
    done_text.grid() 
    time.sleep(1)   
    go_to_confirmation(show_page)

def paymentError():
    simulate_error_btn.grid_remove()
    simulate_success_btn.grid_remove()
    retry_payment_btn.grid()   

def retryPayment():
    print("Retrying!")
    retry_payment_btn.grid_remove()  
    simulate_error_btn.grid()
    simulate_success_btn.grid()
     