import kivy
import kivymd
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, SwapTransition
from kivymd.app import MDApp
from kivymd.toast import toast

from pymongo import MongoClient

from homepage import products
from records import user_table, hijab_table, abaya_table

import numpy as np

Window.size = (500, 700)

class HijabApp(MDApp):

    image = []

    client = MongoClient("localhost", 27017)
    myDb = client.get_database("HijabShop")
    myCollection = myDb.get_collection("Users")

    def build(self):
        self.title = "F&M Clothing"

        global screen_manager
        screen_manager = ScreenManager(transition = SwapTransition())

        screen_manager.add_widget(Builder.load_file("products.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("homepage.kv"))
        screen_manager.add_widget(Builder.load_file("update_user.kv"))
        screen_manager.add_widget(Builder.load_file("confirm_order.kv"))
        screen_manager.add_widget(Builder.load_file("cart.kv"))
        screen_manager.add_widget(Builder.load_file("product_screen.kv"))
        screen_manager.add_widget(Builder.load_file("done.kv"))
        screen_manager.add_widget(Builder.load_file("cart.kv"))
        screen_manager.add_widget(Builder.load_file("bill.kv"))
        screen_manager.add_widget(Builder.load_file("records.kv"))
        screen_manager.add_widget(Builder.load_file("order_placed.kv"))
        screen_manager.add_widget(Builder.load_file("admin.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))

        return screen_manager


    def on_start(self):
        Clock.schedule_interval(self.change_ad, 5)
        products(self)
        user_table(self)
        hijab_table(self)
        abaya_table(self)
        print(kivy.version)
        print(kivymd.__version__)

    def change_ad(self, *args):
        caroused = screen_manager.get_screen("homepage").ids.carousel
        caroused.load_next(mode = next)

    def fetch_data(self, email, password):
        if len(email.text) == 0:
            toast("Invaid Details")

        else:
            for user in self.myCollection.find({"E-Mail" : email.text}):
                if email.text == user.get("E-Mail") and password.text == user.get("Password"):
                    screen_manager.current = "homepage"
                    email.text = " "
                    password.text = " "
                else:
                    toast("Invalid Details")

    def fetch_admin(self, email, password):
        if email.text == "admin" and password.text == "admin":
            screen_manager.current = "admin"
            email.text = " "
            password.text = " "

    def open_product(self):
        screen_manager.current = "cart"

if __name__ == "__main__":
    HijabApp().run()