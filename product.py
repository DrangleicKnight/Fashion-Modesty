from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivymd.toast import toast
from kivymd.toast.kivytoast.kivytoast import Toast
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineAvatarIconListItem, ImageLeftWidget, OneLineListItem, IconRightWidget
from pymongo import MongoClient

product_items = []

client = MongoClient("localhost", 27017)
database = client.get_database("HijabShop")
hijabCollection = database.get_collection("Hijabs")
abayaCollection = database.get_collection("Abayas")

def game_info(self, name):
    self.root.current = "product_screen"
    screen = self.root.get_screen("product_screen").ids

    for hijab in hijabCollection.find({"Name" : name}):
        screen.image.source = hijab.get("Image")
        screen.name.text = hijab.get("Name")
        screen.desc.text = hijab.get("Details")
        screen.price.text = hijab.get("Price")

    for abaya in abayaCollection.find({"Name" : name}):
        screen.image.source = abaya.get("Image")
        screen.name.text = abaya.get("Name")
        screen.desc.text = abaya.get("Details")
        screen.price.text = abaya.get("Price")

def add_to_cart(self, name, price, img):

    screen = self.root.get_screen("cart").ids.list
    total =  self.root.get_screen("cart").ids.price
    totalConfirm = self.root.get_screen("confirm_order").ids.price

    item = OneLineAvatarIconListItem(text = name.text, theme_text_color = "Custom", text_color = (0, 0, 0, 1))
    image = ImageLeftWidget(size_hint = (2.5, 1))
    icon = IconRightWidget(icon = "trash-can", theme_text_color = "Custom", text_color = (0, 0, 0, 1),
                           on_press = lambda a: [sorting(self, item, price), sorting2(self, name.parent)])
    label = MDLabel(text = price.text, pos_hint = {"center_x" : .8, "center_y" : .5}, halign = "center",
                    theme_text_color = "Custom", text_color = (0, 0, 0, 1))
    image.source = img.source

    item.add_widget(image)
    item.add_widget(label)
    item.add_widget(icon)

    screen.add_widget(item)

    product_items.append(price.text)
    toast(f"{name.text} added to cart")

    total_amount = str(sum(map(int, product_items)))

    total.text = "Total: " + total_amount + "Rs/-"
    totalConfirm.text = "Total: " + total_amount + "Rs/-"

def sorting(self, item, price):
    screen = self.root.get_screen("cart").ids.list
    total = self.root.get_screen("cart").ids.price
    totalConfirm = self.root.get_screen("confirm_order").ids.price

    screen.remove_widget(item)
    product_items.remove(price.text)

    total_amount = sum(map(int, product_items))

    total.text = "Total: " + str(total_amount) + "Rs/-"
    totalConfirm.text = "Total: " + str(total_amount) + "Rs/-"

def sorting2(self, item):
    screen = self.root.get_screen("bill").ids.list
    screen.remove_widget(item)

def add_to_bill(self, name, price):
    screen = self.root.get_screen("bill").ids.list
    item = OneLineListItem(text=name.text)
    label = MDLabel(text=f"{price.text}/-", pos_hint={"center_x": .85, "center_y": .5}, halign="center")
    item.add_widget(label)
    screen.add_widget(item)