# Import Hell
from unittest import case

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
import datetime as dt

class Statistics(Screen):
    def __init__(self, **kwargs):
        super(Statistics, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")
        self.log = TextInput(readonly=True)
        layout.add_widget(self.log)
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
        # Drop Down
        self.dropdown = DropDown()
        self.filter_button = Button(text="Filter", size_hint=(0.3, 0.1), on_release=self.dropdown.open, pos_hint={"right": 1, "top": 1})
        self.all_time = Button(text="All Time", size_hint_y=None, height=80)
        self.all_time.bind(on_release=self.on_button_click)
        self.year = Button(text="Today", size_hint_y=None, height=80)
        self.year.bind(on_release=self.on_button_click)
        self.month = Button(text="Last 7 Days", size_hint_y=None, height=80)
        self.month.bind(on_release=self.on_button_click)
        self.week = Button(text="Last 30 Days", size_hint_y=None, height=80)
        self.week.bind(on_release=self.on_button_click)
        self.day = Button(text="Last 90 Days", size_hint_y=None, height=80)
        self.day.bind(on_release=self.on_button_click)
        self.day2 = Button(text="Last 6 Months", size_hint_y=None, height=80)
        self.day2.bind(on_release=self.on_button_click)
        self.dropdown.add_widget(self.all_time)
        self.dropdown.add_widget(self.year)
        self.dropdown.add_widget(self.month)
        self.dropdown.add_widget(self.week)
        self.dropdown.add_widget(self.day)
        self.add_widget(self.filter_button)
        self.add_widget(self.dropdown)
        self.dropdown.dismiss()
        self.load_data()

    def on_button_click(self, button):
        text = button.text
        match text:
            case "Timer":
                self.manager.current = "timer"
            case "Statistics":
                self.manager.current = "statistics"
            case "All Time":
                self.load_data()
                self.dropdown.dismiss()
            case "Today":
                self.filter_time(day=1)
            case "Last 7 Days":
                self.filter_time(day=7)
            case "Last 30 Days":
                self.filter_time(day=30)
            case "Last 90 Days":
                self.filter_time(day=90)
            case "Last 6 Months":
                self.filter_time(day=182)

    def filter_time(self, day):
        self.dropdown.dismiss()
        user_data = App.get_running_app().user_data
        date_format = "%Y-%m-%d %H:%M:%S"
        now = datetime.now()
        total_text = ""
        if day == 1:
            time_period = now - dt.timedelta(days=1)
        elif day == 7:
            time_period = now - dt.timedelta(days=7)
        elif day == 30:
            time_period = now - dt.timedelta(days=30)
        elif day == 90:
            time_period = now - dt.timedelta(days=90)
        elif day == 182:
            time_period = now - dt.timedelta(days=182)
        else:
            print("idk brug")
        for date in user_data:
            date_obj = datetime.strptime(date[:19], date_format)
            seconds_since_epoch = user_data[date]["timestamp"]
            button_pressed = user_data[date]["button_pressed"]
            if date_obj > time_period:
                total_text += f"{self.get_readable_date(date)}: {button_pressed}\n"
        self.log.text = total_text

    def load_data(self):
        user_data = App.get_running_app().user_data
        total_text = ""
        for date in user_data:
            seconds_since_epoch = user_data[date]["timestamp"]
            button_pressed = user_data[date]["button_pressed"]
            total_text += f"{self.get_readable_date(date)}: {button_pressed}\n"
        self.log.text = total_text

    def get_readable_date(self, date):
        raw_month = date[5:7]
        month = "Didn't Assign"
        match raw_month:
            case "01":
                month = "January"
            case "02":
                month = "February"
            case "03":
                month = "March"
            case "04":
                month = "April"
            case "05":
                month = "May"
            case "06":
                month = "June"
            case "07":
                month = "July"
            case "08":
                month = "August"
            case "09":
                month = "September"
            case "10":
                month = "October"
            case "11":
                month = "November"
            case "12":
                month = "December"
            case _:
                month = "Error"
        day = date[8:10]
        if day[0] == "0":
            day = day[1]
        year = date[0:4]
        hour = date[11:13]
        if int(hour) < 12:
            hour_modifier = "AM"
            if int(hour) < 10:
                hour = hour[0]
        else:
            hour = int(hour) // 12
            hour_modifier = "PM"
        minutes = date[14:16]


        return f"{month} {day}, {year} at {hour}:{minutes} {hour_modifier}"
