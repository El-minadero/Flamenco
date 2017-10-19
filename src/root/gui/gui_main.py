import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label

kivy.require("1.10.0")


class GuiMainApp(App):
    
    def __init__(self,controller,**kwargs):
        super().__init__(**kwargs)
        self.wheel      = Wheel(**kwargs)
        self.controller = controller
        
    def build(self):
        return Wheel()
        '''
        label = Label(text="SEAN")
        layout = BoxLayout()
        layout.add_widget(label, 0)
        return layout
        '''
class Wheel(Widget):
    '''
       The All-Powerful Flamenco Wheel
       Some functions that need defining:
       -rotate forward,backward
       
       Some variables that need defining:
       - family list
       -
    '''


    def __init__(self,**kwargs):
        '''
        Constructor
        '''
        super().__init__(**kwargs)
        print("making Wheel")
        self._init_wheel(**kwargs)
        
    def _init_wheel(self,**kwargs):
        if kwargs is None:
            pass
        else:
            pass
            
    def _rotate(self):
        pass