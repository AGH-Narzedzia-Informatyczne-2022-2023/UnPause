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
        print("To jest coś co wywoła konflikt interesów")
        for i in range(3):
            print(i)
            pass
        print("tak albo nie")
        for i in range(5):
            btn = Button(text="Button #%s" % (i+1),
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)
        return layout


class EntryScreen(Screen):
    pass


class SomeBoxes(BoxLayout):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]
        print("To jest coś co wywoła konflikt interesów")
        for i in range(3):
            print(i)
            pass
        print("tak albo nie")
        for i in range(5):
            btn = Button(text="Button #%s" % (i+1),
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)
        return layout


class Functions(Screen):
    pass


class SomeKoox(BoxLayout):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]
        print("To jest coś co wywoła konflikt interesów")
        for i in range(3):
            print(i)
            pass
        print("tak albo nie")
        for i in range(5):
            btn = Button(text="Button #%s" % (i+1),
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)
        return layout


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(EntryScreen(name='entry'))
        sm.add_widget(Functions(name='functions'))

        return sm


if __name__ == '__main__':
    MainApp().run()
