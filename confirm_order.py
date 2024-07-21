import mimetypes
import shutil
import smtplib
from datetime import date, datetime
from email.message import EmailMessage

from kivy.core.window import Window
from pymongo import MongoClient

from product import product_items

total_amount = str(sum(map(int, product_items)))

client = MongoClient("localhost", 27017)
myDB = client.get_database("HijabShop")
myCollection = myDB.get_collection("Users")

emailUser = []

def generate_bill(self, name, address, contact, email, price):

    emailUser.append(email.text)

    today = date.today().strftime("%d-%m-%Y")
    time = datetime.now()

    hour = time.hour
    minute = time.minute

    screen = self.root.get_screen("bill").ids

    screen.bill_no.text = f"Bill No : {contact.text[0:5]}"
    screen.info.text = f"{name.text}\n{address.text}\n{contact.text}\n{email.text}"
    screen.date.text = f"Date : {today}"
    screen.time.text = f"Time : {hour}:{minute} "
    screen.price.text = price.text

def take_screen(bill_no):
    file_name = Window.screenshot(f"images/Bill/Bill_No_{bill_no.text[10:15]}.jpg")
    name_parts = file_name.split('.')
    new_name = ''.join([name_parts[0][:-4], '.', name_parts[1]])
    shutil.move(file_name, new_name)


def send_mail(bill_no):
    message = EmailMessage()
    sender = "youremail"
    recipient = emailUser[0]

    message['From'] = sender
    message['To'] = recipient

    message['Subject'] = "Thank you for purchasing from Trubber's Stash"

    message.set_content("Your order will arrive in 3-5 working days!\n\nPlease check out more games from our shop")
    mime_type, _ = mimetypes.guess_type(f"images/Bill/Bill_No{bill_no.text[10:15]}.jpg")
    mime_type, mime_subtype = mime_type.split('/')
    with open(f'images/Bill/Bill_No_{bill_no.text[10:15]}.jpg', 'rb') as file:
        message.add_attachment(file.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=f'Bill_No_{bill_no.text[10:15]}.jpg')
    print(message)
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.set_debuglevel(1)
    mail_server.login("yourmail", "rinyoydupgmhwiog")
    mail_server.send_message(message)
    mail_server.quit()
