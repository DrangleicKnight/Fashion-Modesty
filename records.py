from kivy.metrics import dp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
database = client.get_database("HijabShop")

userCollection = database.get_collection("Users")
hijabCollection = database.get_collection("Hijabs")
abayaCollection = database.get_collection("Abayas")

# user details
email = []
f_name = []
l_name = []
contact = []
address = []

for user in userCollection.find():
    email.append(user.get("E-Mail"))
    f_name.append(user.get("First Name"))
    l_name.append(user.get("Last Name"))
    contact.append(user.get("Contact"))
    address.append(user.get("Address"))


def user_table(self):
    global datatable
    self.theme_cls.theme_style = "Dark"
    self.theme_cls.primary_palette = "Amber"

    screen = self.root.get_screen("records").ids.layout

    datatable = MDDataTable(use_pagination=True,
                            column_data=[("Email", dp(45)),
                                         ("Name", dp(30)),
                                         ("Contact", dp(20)),
                                         ("Address", dp(40))],

                            row_data=[(email[i],
                                       f_name[i] + " " + l_name[i],
                                       contact[i],
                                       address[i])
                                      for i in range(len(f_name))])

    datatable.on_row_press = on_check_press

    screen.add_widget(datatable)


# hijab details
name = []
price = []
quantity = []

for game_info in hijabCollection.find():
    name.append(game_info.get("Name"))
    price.append(game_info.get("Price"))
    quantity.append(game_info.get("Quantity"))

def hijab_table(self):
    self.theme_cls.theme_style = "Dark"
    self.theme_cls.primary_palette = "Orange"

    layout =self.root.get_screen("records").ids.layout2

    carousel = self.root.get_screen("records").ids.carousel

    datatable = MDDataTable(use_pagination = True,
                            column_data = [("Product Name", dp(40)),
                                           ("Price", dp(30)),
                                           ("Quantity", dp(50))],

                            row_data = [(name[i],
                                         price[i],
                                         quantity[i])
                                        for i in range(len(name))])
    datatable.on_check_press = on_check_press

    layout.add_widget(datatable)


# abaya details
nameA = []
priceA = []
quantityA = []

for game_info in hijabCollection.find():
    nameA.append(game_info.get("Name"))
    priceA.append(game_info.get("Price"))
    quantityA.append(game_info.get("Quantity"))

def abaya_table(self):
    self.theme_cls.theme_style = "Dark"
    self.theme_cls.primary_palette = "Orange"

    layout = self.root.get_screen("records").ids.layout3

    carousel = self.root.get_screen("records").ids.carousel

    datatable = MDDataTable(use_pagination = True,
                            column_data = [("Product Name", dp(40)),
                                           ("Price", dp(30)),
                                           ("Quantity", dp(50))],

                            row_data = [(nameA[i],
                                         priceA[i],
                                         quantityA[i])
                                        for i in range(len(nameA))])
    datatable.on_check_press = on_check_press

    layout.add_widget(datatable)

def on_check_press(row):
    popup = MDDialog(text = "What would you like to do?",
                     buttons = [MDRaisedButton(text = "Delete"),
                     MDRaisedButton(text = "Update")])

    popup.open()