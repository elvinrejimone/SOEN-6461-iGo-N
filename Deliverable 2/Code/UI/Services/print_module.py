from PIL import Image, ImageDraw, ImageFont
import qrcode
import tkinter as tk
from PIL import ImageTk
import os

top_banner_image_path = "./Assets/iGoBannerMAIN.png"
bottom_banner_image_path= "./Assets/iGoBannerBottom.png"

def generate_ticket(ticket_details):
    print("Generating Ticket Print!")
    # Set up the image
    width = 600
    height = 500
    banner_height = 100
    bottom_banner_height = 175
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    # Add the top banner image
    top_banner_img = Image.open(top_banner_image_path)
    top_banner_img = top_banner_img.resize((width, banner_height), resample=Image.LANCZOS)
    img.paste(top_banner_img, (0, 0))

    # Add the bottom banner image
    bottom_banner_img = Image.open(bottom_banner_image_path)
    bottom_banner_img = bottom_banner_img.resize((width, bottom_banner_height), resample=Image.LANCZOS)
    img.paste(bottom_banner_img, (0, height - bottom_banner_height))

    # Add the ticket details
    details_font = ImageFont.truetype('arial.ttf', size=15)
    small_font = ImageFont.truetype('times.ttf', size=10)
    details_text_color = 'black'
    details_text_x = 40
    details_text_y = banner_height + 40
    for key, value in ticket_details.items():
        font = details_font
        det_x = details_text_x
        if(key == "Details"):
            font = small_font
            det_x = 30
        details_text = f'{key}: {value}'
        if(key == "Billet" or key == "Ticket"):
            details_text = f'{value}'
        draw.text((det_x, details_text_y), details_text, fill=details_text_color, font=font)
        details_text_y += 30

    # Add the QR code
    qr_code_size = 150
    qr_code = qrcode.QRCode(version=None, box_size=10, border=4)
    qr_code.add_data(str(ticket_details))
    qr_code.make(fit=True)
    qr_code_img = qr_code.make_image(fill_color='#20bebe', back_color='white').resize((qr_code_size, qr_code_size))
    img.paste(qr_code_img, (width - qr_code_size - 40, banner_height + 40))

    # Save the image
    save_path = "./Services/Tickets"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    filename = os.path.join(save_path, f'{ticket_details["Ticket-ID"]}.png')
    img.save(filename)
    print("Printed Ticket")
    return img
