import kivy
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from datetime import datetime
import datetime as dt
kivy.require("2.3.1")

from App_Module import format_delta_time

class Timer(Screen):
    def __init__(self, **kwargs):
        # Setup
        super(Timer, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")
        # Fasting Text Input
        self.fasting_time = TextInput(multiline=False, readonly=True, font_size=100)
        layout.add_widget(self.fasting_time)
        # Button
        self.fasting_button = Button(text="Start Eating", font_size=60)
        self.fasting_button.bind(on_release=self.on_button_click)
        layout.add_widget(self.fasting_button)
        # Screen Change Buttons
        self.timer_button = Button(text="Timer", font_size=60)
        self.timer_button.bind(on_release=self.on_button_click)
        self.stats_button = Button(text="Statistics", font_size=60)
        self.stats_button.bind(on_release=self.on_button_click)
        # Grid Setup
        grid = GridLayout(cols=2)
        grid.add_widget(self.timer_button)
        grid.add_widget(self.stats_button)
        grid.size_hint_y = 0.25
        layout.add_widget(grid)
        # Timer Setup
        user_data = App.get_running_app().user_data
        # Get Last Entry in user_data
        if user_data:
            for date in user_data:
                self.last_timestamp = user_data[date]["timestamp"]
        else:
            self.last_timestamp = time.time()
        self.update_timer()
        Clock.schedule_interval(self.update_timer, 1)
        # Add Layout
        self.add_widget(layout)

    def on_button_click(self, button):
        match button.text:
            case "Start Eating":
                button.text = "Stop Eating"
                App.get_running_app().user_data.put(str(datetime.now()), timestamp=time.time(), button_pressed=button.text)
                self.last_timestamp = time.time()
                self.manager.get_screen("statistics").load_data()
            case "Stop Eating":
                button.text = "Start Eating"
                App.get_running_app().user_data.put(str(datetime.now()), timestamp=time.time(), button_pressed=button.text)
                self.last_timestamp = time.time()
                self.manager.get_screen("statistics").load_data()
            case "Timer":
                self.manager.current = "timer"
            case "Statistics":
                self.manager.current = "statistics"


    def update_timer(self, *args):
        delta_time = time.time() - self.last_timestamp
        time_obj = dt.timedelta(seconds=delta_time)
        self.fasting_time.text = format_delta_time(time_obj)
