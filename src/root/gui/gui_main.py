import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

kivy.require("1.10.0")

class GuiMainApp(App):
    
    def __init__(self,controller,**kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        
        ''' def build(self):
        label = Label(text="SEAN")
        layout = BoxLayout()
        layout.add_widget(label, 0)
        return layout
        '''