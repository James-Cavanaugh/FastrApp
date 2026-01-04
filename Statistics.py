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

from datetime import datetime

class Statistics(Screen):
    def __init__(self, **kwargs):
        super(Statistics, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        self.log = TextInput(readonly=True)
        self.layout.add_widget(self.log)
        # Screen Change Buttons
        self.timer_button = Button(text="Timer")
        self.timer_button.bind(on_release=self.on_button_click)
        self.stats_button = Button(text="Statistics")
        self.stats_button.bind(on_release=self.on_button_click)
        self.grid = GridLayout(cols=2)
        self.grid.add_widget(self.timer_button)
        self.grid.add_widget(self.stats_button)
        self.grid.size_hint_y = 0.25
        self.layout.add_widget(self.grid)
        self.add_widget(self.layout)
        self.load_data()

    def on_button_click(self, button):
        text = button.text
        if text == "Timer":
            self.manager.current = "timer"
        elif text == "Statistics":
            self.manager.current = "statistics"

    def load_data(self):
        user_data = App.get_running_app().user_data
        total_text = ""
        for date in user_data:
            seconds_since_epoch = user_data[date]["timestamp"]
            button_pressed = user_data[date]["button_pressed"]
            total_text += date + ": " + button_pressed + "\n"
        self.log.text = total_text