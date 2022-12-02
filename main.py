import kivy
import random

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

sm = ScreenManager()


class SomeBox(BoxLayout):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]
        ez = True
        for i in range(5):
            btn = Button(text="Button #%s" % (i+1),
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)
        return layout


class EntryScreen(Screen):
    pass


class Functions(Screen):
    pass


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(EntryScreen(name='entry'))
        sm.add_widget(Functions(name='functions'))

        return sm


if __name__ == '__main__':
    MainApp().run()
