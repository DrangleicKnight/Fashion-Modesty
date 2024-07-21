from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
myDatabase = client.get_database("HijabShop")
myCollection = myDatabase.get_collection("Users")

selected_mail = []

error = MDDialog(size_hint=(.5, .15), pos_hint={"center_x": .5, "center_y": .5}, text="User doesn't exist",
                        buttons=[MDFlatButton(text="Dismiss", theme_text_color  = "Custom", text_color = "black",
                        on_press=lambda a: error.dismiss())])

def fetch_user(account_name, email, first_name, last_name, contact, address):
    selected_mail.clear()
    if myCollection.find_one({"E-Mail" : email.text}):
        selected_mail.append(email.text)

        for user in myCollection.find({"E-Mail" : email.text}):
            account_name.text = f"{user.get('First Name')}'s Account"
            first_name.text = user.get("First Name")
            last_name.text = user.get("Last Name")
            contact.text = user.get("Contact")
            address.text = user.get("Address")
    else:
        error.open()
        first_name.text = ""
        last_name.text = ""
        email.text = ""
        contact.text = ""
        address.text = ""

def update_user(email, first_name, last_name, contact, address):
    if len(selected_mail) > 0:
        myCollection.update_one({"E-Mail" : selected_mail[0]}, {"$set" : {"E-Mail" : email.text,
                                                                               "First Name" : first_name.text,
                                                                               "Last Name" : last_name.text,
                                                                               "Contact" : contact.text,
                                                                               "Address" : address.text}})
        toast("User Updated")
    else:
        error.open()

def delete_user(email, first_name, last_name, contact, address):
    if len(selected_mail) > 0:
        myCollection.delete_one({"E-Mail" : selected_mail[0]})
        toast("User Deleted")
    else:
        error.open()
        first_name.text = ""
        last_name.text = ""
        email.text = ""
        contact.text = ""
        address.text = ""