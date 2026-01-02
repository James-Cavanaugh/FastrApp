# Import Hell
import kivy
kivy.require("2.3.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Fastr(BoxLayout):
    def __init__(self, **kwargs):
        super(Fastr, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="Fastr"))
        self.fasting_time = TextInput(multiline=False, readonly=True)
        self.add_widget(self.fasting_time)
        grid = GridLayout(cols=2, rows=2)
        self.start_fasting = Button(text="Start")
        self.stop_fasting = Button(text="Stop")
        grid.add_widget(self.start_fasting)
        grid.add_widget(self.stop_fasting)
        self.add_widget(grid)

    def button_click(self, button):
        text = button.text
        if text == "Start":
            pass
        elif text == "Stop":
            pass




class MainApp(App):
    def build(self):
        return Fastr()

if __name__ == '__main__':
    MainApp().run()