import kivy
from kivy.app import App
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import ScreenManager, Screen
from Timer import Timer
from Statistics import Statistics
kivy.require("2.3.1")

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