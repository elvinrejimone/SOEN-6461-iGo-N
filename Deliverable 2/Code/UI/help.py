import tkinter as tk

# Define the FAQs and contact information
faqs = {
    "What do I do if my credit/debit card is declined at the vending machine?": "If your card is declined, you can try using a different card or paying with cash. If the problem persists, you may need to contact your card issuer for assistance.",
    "Can I get a refund if I change my mind or miss my ferry?": "No, tickets purchased at the vending machine are non-refundable. Make sure you choose the correct ticket type and departure time before completing your purchase.",
    "Can I use a gift card or voucher to buy a ferry ticket at the vending machine?": "No, the vending machine does not accept gift cards or vouchers as payment for ferry tickets. You can use cash or a credit/debit card instead.",
    "What happens if I lose my ticket after buying it at the vending machine?": "Unfortunately, lost tickets cannot be replaced. You will need to purchase a new ticket at the vending machine or at the ticket booth.",
    "What do I do if the vending machine is out of order or not working properly?": "If the vending machine is not working, you can purchase your ticket at the ticket booth or ask a ferry employee for assistance.",
    "What should I do if I have a problem with my ferry ticket purchase?": "If you experience any issues with your ticket purchase, you can contact customer service for assistance. The phone number and email address should be displayed on the vending machine or at the ticket booth."
}

contact_info = "Email: support@iGo.com\nPhone: +1(123)456-7890"

# Define a function to display the FAQs and contact information
def show_faq():
    # Hide the Help button
    help_button.pack_forget()

    # Create a frame to hold the FAQs and contact information
    faq_frame = tk.Frame(root)

    # Add the FAQs to the frame
    for i, (question, answer) in enumerate(faqs.items()):
        tk.Label(faq_frame, text=f"{i+1}. {question}", font=("Arial", 12, "bold")).pack()
        tk.Label(faq_frame, text=answer, font=("Arial", 12)).pack()

    # Add the contact information to the frame
    tk.Label(faq_frame, text="\nContact Information:", font=("Arial", 14, "bold")).pack()
    tk.Label(faq_frame, text=contact_info, font=("Arial", 12)).pack()

    # Add a Back button to the frame
    back_button = tk.Button(faq_frame, text="Back", font=("Arial", 12), command=lambda: hide_faq(faq_frame, back_button))
    back_button.pack(pady=10)

    # Pack the frame
    faq_frame.pack(pady=20)

# Define a function to hide the FAQs and contact information and show the Help button
def hide_faq(faq_frame, back_button):
    # Destroy the FAQs and contact information frame
    faq_frame.destroy()

    # Show the Help button
    help_button.pack()

# Create the root window
root = tk.Tk()
root.title("Ferry FAQs")

# Create a Help button
help_button = tk.Button(root, text="Help", font=("Arial", 16), command=show_faq)
help_button.pack(pady=20)

# Run the GUI
root.mainloop()
