import tkinter as tk
from utils import *
SMALL_FONT =("Verdana", 20)

class HelpPopup:
    def __init__(self, faqs, contact_info, lang='en'):
        self.root = tk.Tk()
        self.root.title("Help")
        self.root.geometry("900x600")
        self.faqs = faqs[getState("language")]
        self.contact_info = contact_info
        self.lang = lang

        self.label = tk.Label(self.root, text=getAppWord("faqs"))
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(self.root, width=200, height=20)
        self.listbox.pack(pady=1)

        for key in self.faqs:
            if self.lang == 'fr':
                self.listbox.insert(tk.END, self.faqs_fr[key])
            else:
                self.listbox.insert(tk.END, key)

            self.listbox.insert(tk.END, self.faqs[key])
            self.listbox.insert(tk.END, '')

        self.contact_label = tk.Label(self.root, text=self.contact_info)
        self.contact_label.pack(pady=10)
        
        self.assist_label = tk.Label(self.root, text=getAppWord("HelpOntheWay"), font=SMALL_FONT)


        self.assist_button = tk.Button(self.root, text=getAppWord("seekAssistance"), command=lambda : callAssistance(self), font="Raleway", bg="#57467b", fg="white", height=2, width=20)
        self.assist_button.pack(pady=10)        

        self.button = tk.Button(self.root, text=getAppWord("cancel"), command=self.root.destroy, font="Raleway", bg="#57467b", fg="white", height=2, width=20)
        self.button.pack(pady=10)

    def show(self):
        self.root.mainloop()

def show_help_popup():
    faqs = {
    "english": {
        "What do I do if my credit/debit card is declined at the vending machine?": "If your card is declined, you can try using a different card or paying with cash. If the problem persists, you may need to contact your card issuer for assistance.",
        "Can I get a refund if I change my mind or miss my ferry?": "No, tickets purchased at the vending machine are non-refundable. Make sure you choose the correct ticket type and departure time before completing your purchase.",
        "Can I use a gift card or voucher to buy a ferry ticket at the vending machine?": "No, the vending machine does not accept gift cards or vouchers as payment for ferry tickets. You can use cash or a credit/debit card instead.",
        "What happens if I lose my ticket after buying it at the vending machine?": "Unfortunately, lost tickets cannot be replaced. You will need to purchase a new ticket at the vending machine or at the ticket booth.",
        "What do I do if the vending machine is out of order or not working properly?": "If the vending machine is not working, you can purchase your ticket at the ticket booth or ask a ferry employee for assistance.",
        "What should I do if I have a problem with my ferry ticket purchase?": "If you experience any issues with your ticket purchase, you can contact customer service for assistance. The phone number and email address should be displayed on the vending machine or at the ticket booth."
        },
    "french": {
        "Que dois-je faire si ma carte de crédit/débit est refusée par le distributeur automatique?": "Si votre carte est refusée, vous pouvez essayer d'utiliser une autre carte ou de payer en espèces. Si le problème persiste, vous devrez peut-être contacter l'émetteur de votre carte pour obtenir de l'aide.",
        "Puis-je obtenir un remboursement si je change d'avis ou si je manque mon ferry?": "Non, les billets achetés au distributeur automatique ne sont pas remboursables. Assurez-vous de choisir le bon type de billet et l'heure de départ avant de finaliser votre achat.",
        "Puis-je utiliser une carte-cadeau ou un bon d'achat pour acheter un billet de ferry au distributeur automatique?": "Non, le distributeur automatique n'accepte pas les cartes-cadeaux ou les bons d'achat comme mode de paiement pour les billets de ferry. Vous pouvez utiliser des espèces ou une carte de crédit/débit à la place.",
        "Que se passe-t-il si je perds mon billet après l'avoir acheté au distributeur automatique?": "Malheureusement, les billets perdus ne peuvent pas être remplacés. Vous devrez acheter un nouveau billet au distributeur automatique ou au guichet.",
        "Que dois-je faire si le distributeur automatique est hors service ou ne fonctionne pas correctement?": "Si le distributeur automatique ne fonctionne pas, vous pouvez acheter votre billet au guichet ou demander l'aide d'un employé du ferry.",
        "Que dois-je faire si j'ai un problème avec mon achat de billet de ferry?": "Si vous rencontrez des problèmes avec votre achat de billet, vous pouvez contacter le service clientèle pour obtenir de l'aide. Le numéro"
        }
    }


    contact_info = "Email: support@iGo.com\nPhone: +1(123)456-7890"

    popup = HelpPopup(faqs, contact_info)
    popup.show()

def callAssistance(self):
    print("Called Assistance!")
    self.assist_button.pack_forget()
    self.assist_label.pack(pady=10)