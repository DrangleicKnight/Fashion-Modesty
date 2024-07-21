from pymongo import MongoClient

client = MongoClient("localhost", 27017)
myDb = client.get_database("HijabShop")
myCollection = myDb.get_collection("Users")

def next1(self):
    carousel = self.root.get_screen("main").ids.caroused
    carousel.load_next(mode=next)
    self.root.get_screen("main").ids.circle1.icon = "check-decagram"
    self.root.get_screen("main").ids.circle1.theme_text_color = "Custom"
    self.root.get_screen("main").ids.circle1.text_color = self.theme_cls.primary_color
    self.root.get_screen("main").ids.progress.value = 100

def prev(self):
    carousel = self.root.get_screen("main").ids.caroused
    self.root.get_screen("main").ids.circle1.icon = "numeric-1-circle"
    self.root.get_screen("main").ids.circle1.theme_text_color = "Custom"
    self.root.get_screen("main").ids.circle1.text_color = "black"
    self.root.get_screen("main").ids.progress.value = 0
    carousel.load_previous()

def submit(self):
    carousel = self.root.get_screen("main").ids.caroused
    carousel.load_next(mode=next)
    self.root.get_screen("main").ids.circle2.icon = "check-decagram"
    self.root.get_screen("main").ids.circle2.theme_text_color = "Custom"
    self.root.get_screen("main").ids.circle2.text_color = self.theme_cls.primary_color

def insert(f_name, l_name, contact, email, password, address):
    myCollection.insert_one({
        "First Name" : f_name.text,
        "Last Name" : l_name.text,
        "Contact" : contact.text,
        "E-Mail" : email.text,
        "Password" : password.text,
        "Address" : address.text
    })
