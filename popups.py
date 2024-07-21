from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivymd.toast import toast
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.menu import MDDropdownMenu
from pymongo import MongoClient

image = []

client = MongoClient("localhost", 27017)
myDb = client.get_database("HijabShop")
myCollectionHijab = myDb.get_collection("Hijabs")
myCollectionAbayas = myDb.get_collection("Abayas")

def popup(self):
    popup = Popup(size_hint=(.8, .6), title="Select Picture")
    filechooser = FileChooserIconView()
    filechooser.add_widget(MDRoundFlatButton(text="Select",
                                             size_hint=(.4, .1),
                                             pos_hint={"center_x": .5},
                                             md_bg_color=(0, 0, 0, .5),
                                             on_press=lambda a: getImage(self, filechooser.selection)
                                             ))
    popup.add_widget(filechooser)
    popup.open()

def getImage(self, file):
    picture = "".join(file)
    image.append(picture)

    screen = self.root.get_screen("products").ids.prod_image
    screen.source = picture

    print(picture)

def add_product(type, name, details, price, quantity):

    if type.text == "Hijab":
        myCollectionHijab.insert_one({
            "Name" : name.text,
            "Details" : details.text,
            "Price" : price.text,
            "Quantity" : quantity.text,
            "Image" : image[0]
        })
    elif type.text == "Abaya":
        myCollectionAbayas.insert_one({
            "Name" : name.text,
            "Details" : details.text,
            "Price" : price.text,
            "Quantity" : quantity.text,
            "Image" : image[0]
        })
    toast("Product Added!")
    image.clear()


# This is to select the type of the product
def dropup(self):
    screen = self.root.get_screen("products").ids.type

    def text1():
        screen.text = "Hijab"
        dropdown.dismiss()
        print(screen.text)

    def text2():
        screen.text = "Abaya"
        dropdown.dismiss()
        print(screen.text)

    items1 = [
        {
            "viewclass": "OneLineListItem",
            "text": "Hijab",
            "on_press": lambda: text1()
        },
        {
            "viewclass": "OneLineListItem",
            "text": "Abaya",
            "on_press": lambda: text2()
        }
    ]
    dropdown = MDDropdownMenu(items=items1,
                              width_mult=2,
                              max_height=100,
                              pos_hint={"center_x": .5, "center_y": .5})

    dropdown.caller = screen
    dropdown.open()

def show_toast():
    toast("Item Added to Cart")