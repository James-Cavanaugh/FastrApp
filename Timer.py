# Import Hell
import kivy
import time
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

from datetime import datetime

class Timer(BoxLayout):
    def __init__(self, **kwargs):
        # Setup
        super(Timer, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.user_data = JsonStore("user_data.json", indent=4)
        # Fasting Text Input
        self.fasting_time = TextInput(multiline=False, readonly=True)
        self.add_widget(self.fasting_time)
        # Button
        self.fasting_button = Button(text="Start Eating")
        self.fasting_button.bind(on_release=self.on_button_click)
        self.add_widget(self.fasting_button)
        # Screen Change Buttons
        self.timer_button = Button(text="Timer")
        self.stats_button = Button(text="Statistics")

    def on_button_click(self, button):
        text = button.text
        self.user_data.put(str(datetime.now()), timestamp=time.time(), button_pressed=text)
        if text == "Start Eating":
            button.text = "Stop Eating"
        elif text == "Stop Eating":
            button.text = "Start Eating"

    def on_start(self):
        print("its starting")

    def on_stop(self):
        print("stopping app")



class MainApp(App):
    def build(self):
        return Timer()

if __name__ == '__main__':
    MainApp().run()