# Import Hell
import kivy
import time

from kivy.tools.gallery import screenshots_dir

kivy.require("2.3.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import ScreenManager, Screen

from Timer import Timer
from Statistics import Statistics

class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_data = JsonStore("user_data.json", indent=4)

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Timer(name="timer"))
        screen_manager.add_widget(Statistics(name="statistics"))
        return screen_manager

if __name__ == '__main__':
    MainApp().run()