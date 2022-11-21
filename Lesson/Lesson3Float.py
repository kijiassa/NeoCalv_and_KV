import kivy
from kivy.app import App
from kivy.uix.layout import Layout
from kivy.uix.floatlayout import FloatLayout

class MyFloat(App):
    def build(self):
        return FloatLayout()


if __name__=='__main__':
    MyFloat().run()