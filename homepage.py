from kivymd.uix.button import MDTextButton
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage

from product import product_items

def product_info(self, name):
    screen = self.root.get_screen("product_screen").ids

    hijabs = self.myDb.get_collection("Hijabs")
    abayas = self.myDb.get_collection("Abayas")

    for names in hijabs.find({"Name": name}):
        screen.name.text = names.get("Name")
        screen.desc.text = names.get("Details")
        screen.image.source = names.get("Image")
        screen.price.text = names.get('Price')

    for abaya in abayas.find({"Name": name}):
        screen.name.text = abaya.get("Name")
        screen.desc.text = abaya.get("Details")
        screen.image.source = abaya.get("Image")
        screen.price.text = abaya.get('Price')

    self.root.current = "product_screen"

    print("Hello!")


def open_product(self):
    self.root.current = "cart"

    cart_screen = self.root.get_screen("cart").ids.price
    confirmation = self.root.get_screen("confirm_order").ids.price
    total_price = str(sum(map(int, product_items)))

    cart_screen.text = total_price + " Rs/-"
    confirmation.text = total_price + " Rs/-"


def products(self):
    hijabs = self.myDb.get_collection("Hijabs")
    abayas = self.myDb.get_collection("Abayas")

    hijab_name = []
    hijab_details = []
    hijab_price = []
    hijab_quantity = []
    hijab_image = []

    for hijab in hijabs.find():
        hijab_name.append(hijab.get("Name"))
        hijab_details.append(hijab.get("Details"))
        hijab_price.append(hijab.get("Price"))
        hijab_quantity.append(hijab.get("Quantity"))
        hijab_image.append(hijab.get("Image"))

    abaya_name = []
    abaya_details = []
    abaya_price = []
    abaya_quantity = []
    abaya_image = []

    for abaya in abayas.find():
        abaya_name.append(abaya.get("Name"))
        abaya_details.append(abaya.get("Details"))
        abaya_price.append(abaya.get("Price"))
        abaya_quantity.append(abaya.get("Quantity"))
        abaya_image.append(abaya.get("Image"))

    def generate_hijabs(image, name, desc, price, quantity):
        screen = self.root.get_screen("homepage").ids.hijab_layout
        baseCard = MDCard(size_hint=(None, None), size=(595, 130), radius=[30])
        layout = MDFloatLayout()

        fontName = "fonts/Poppins-SemiBold.ttf"

        product_image = FitImage(size_hint=(None, None), size=(105, 105), radius=[20],
                                 pos_hint={"center_x": .13, "center_y": .5}, source=image)

        product_name = MDTextButton(text=name,
                                    halign="center", pos_hint={"center_x": .4, "center_y": .8},
                                    on_press=lambda a: product_info(self, name))
        product_name.font_name = fontName
        product_name.font_size = "18sp"

        product_description = MDLabel(text=desc,
                                      theme_text_color="Custom",
                                      text_color=(1, 1, 1, .7), pos_hint={"center_x": .78, "center_y": .5})
        product_description.font_name = fontName
        product_description.font_size = "12sp"

        product_price = MDLabel(text=f"Price : {price}Rs/-", font_size="15sp",
                                pos_hint={"center_x": .78, "center_y": .22})
        product_price.font_name = fontName

        product_quantity = MDLabel(text=f"x{quantity}", font_size="20sp", font_name=fontName,
                                   pos_hint={"center_x": 1.4, "center_y": .5})
        product_quantity.font_name = fontName

        layout.add_widget(product_image)
        layout.add_widget(product_name)
        layout.add_widget(product_description)
        layout.add_widget(product_price)
        layout.add_widget(product_quantity)

        baseCard.add_widget(layout)
        screen.add_widget(baseCard)

    def generate_abayas(image, name, desc, price, quantity):
        screen = self.root.get_screen("homepage").ids.abaya_layout
        baseCard = MDCard(size_hint=(None, None), size=(595, 130), radius=[30])
        layout = MDFloatLayout()

        fontName = "fonts/Poppins-SemiBold.ttf"

        product_image = FitImage(size_hint=(None, None), size=(105, 105), radius=[20],
                                 pos_hint={"center_x": .13, "center_y": .5}, source=image)

        product_name = MDTextButton(text=name,
                                    halign="center", pos_hint={"center_x": .4, "center_y": .8},
                                    on_press=lambda a: product_info(self, name))
        product_name.font_name = fontName
        product_name.font_size = "18sp"

        product_description = MDLabel(text=desc,
                                      theme_text_color="Custom",
                                      text_color=(1, 1, 1, .7), pos_hint={"center_x": .78, "center_y": .5})
        product_description.font_name = fontName
        product_description.font_size = "12sp"

        product_price = MDLabel(text=f"Price : {price}Rs/-", font_size="15sp",
                                pos_hint={"center_x": .78, "center_y": .22})
        product_price.font_name = fontName

        product_quantity = MDLabel(text=f"x{quantity}", font_size="20sp", font_name=fontName,
                                   pos_hint={"center_x": 1.4, "center_y": .5})
        product_quantity.font_name = fontName

        layout.add_widget(product_image)
        layout.add_widget(product_name)
        layout.add_widget(product_description)
        layout.add_widget(product_price)
        layout.add_widget(product_quantity)

        baseCard.add_widget(layout)
        screen.add_widget(baseCard)

    for i in range(len(hijab_name)):
        generate_hijabs(hijab_image[i], hijab_name[i], hijab_details[i], hijab_price[i], hijab_quantity[i])

    for i in range(len(abaya_name)):
        generate_abayas(abaya_image[i], abaya_name[i], abaya_details[i], abaya_price[i], abaya_quantity[i])

def clear(self):
    screen = self.root.get_screen("homepage").ids.hijab_layout
    screen2 = self.root.get_screen("homepage").ids.abaya_layout
    screen.clear_widgets()
    screen2.clear_widgets()
    products(self)
