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
from kivy.clock import Clock

from datetime import datetime
import datetime as dt
import threading

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
        # Timer Setup
        user_data = App.get_running_app().user_data
        # I'm sad that I can't think of a better way to do this
        for date in user_data:
            recent = date
        if user_data:
            self.last_timestamp = user_data[recent]["timestamp"]
        else:
            self.last_timestamp = time.time()
        self.run_timer()
        Clock.schedule_interval(self.run_timer, 1)
        # Add Layout
        self.add_widget(layout)

    def on_button_click(self, button):
        text = button.text
        match text:
            case "Start Eating":
                button.text = "Stop Eating"
                App.get_running_app().user_data.put(str(datetime.now()), timestamp=time.time(), button_pressed=text)
                self.last_timestamp = time.time()
            case "Stop Eating":
                button.text = "Start Eating"
                App.get_running_app().user_data.put(str(datetime.now()), timestamp=time.time(), button_pressed=text)
                self.last_timestamp = time.time()
            case "Timer":
                self.manager.current = "timer"
            case "Statistics":
                self.manager.current = "statistics"

    def format_delta_time(self, delta_time):
        hours, remainder = divmod(int(delta_time.seconds), 3600)
        minutes, seconds = divmod(remainder, 60)
        hours += delta_time.days * 24
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


    def run_timer(self, *args):
        delta_time = time.time() - self.last_timestamp
        time_obj = dt.timedelta(seconds=delta_time)
        self.fasting_time.text = self.format_delta_time(time_obj)
