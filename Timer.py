# Import Hell
import kivy
import time

kivy.require("2.3.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen

from datetime import datetime

class Timer(Screen):
    def __init__(self, **kwargs):
        # Setup
        super(Timer, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")
        # Fasting Text Input
        self.fasting_time = TextInput(multiline=False, readonly=True)
        layout.add_widget(self.fasting_time)
        # Button
        self.fasting_button = Button(text="Start Eating")
        self.fasting_button.bind(on_release=self.on_button_click)
        layout.add_widget(self.fasting_button)
        # Screen Change Buttons
        self.timer_button = Button(text="Timer")
        self.timer_button.bind(on_release=self.on_button_click)
        self.stats_button = Button(text="Statistics")
        self.stats_button.bind(on_release=self.on_button_click)
        grid = GridLayout(cols=2)
        grid.add_widget(self.timer_button)
        grid.add_widget(self.stats_button)
        grid.size_hint_y = 0.25
        layout.add_widget(grid)
        self.add_widget(layout)

    def on_button_click(self, button):
        text = button.text
        match text:
            case "Start Eating":
                button.text = "Stop Eating"
                App.get_running_app().user_data.put(str(datetime.now()), timestamp=time.time(), button_pressed=text)
            case "Stop Eating":
                button.text = "Start Eating"
                App.get_running_app().user_data.put(str(datetime.now()), timestamp=time.time(), button_pressed=text)
            case "Timer":
                self.manager.current = "timer"
            case "Statistics":
                self.manager.current = "statistics"

    def run_timer(self):
        pass