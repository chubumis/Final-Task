import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.core.window import Window
from kivy.core.text import LabelBase
Window.clearcolor = (0.5,0,1,1)

'''    canvas.before:
        Color:
            rgba: (0.5,0,0.8,1)
        Rectangle:
            pos: self.pos
            size: self.size
            '''

class BoxLayoutExample(BoxLayout):
    pass
'''
    def __init__(self,**kwargs)
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)
        
'''

class BoxLayoutSequencer(FloatLayout):
    pass

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()

