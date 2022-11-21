import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    nameTh = ObjectProperty(None)
    emailTh = ObjectProperty(None)

    def btn(self):
        print("Name: ", self.nameTh.text, "email: ", self.emailTh.text)
        self.nameTh.text = ''
        self.emailTh.text = ''



class MyApp(App):
    def build(self):
        return MyGrid()


if __name__=="__main__":
    MyApp().run()

