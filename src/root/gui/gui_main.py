import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label

kivy.require("1.10.0")


class GuiMainApp(App):
    
    def __init__(self,**kwargs):
        super().__init__()
        self.wheel      = WheelRoot(**kwargs)
        
    def build(self):
        return self.wheel
        '''
        label = Label(text="SEAN")
        layout = BoxLayout()
        layout.add_widget(label, 0)
        return layout
        '''
class AbstractSpoke():
    
    def __init__(self,**kwargs):
        self.controller = kwargs["controller"]
        self.name       = kwargs["name"]
        
    def _rotate(self,angle):
        pass
            
    def set_selection(self):
        self.controller.setSelection(self.name)
        
class WheelRoot(Widget,AbstractSpoke):
    '''
       The All-Powerful Flamenco Wheel
       Some functions that need defining:
       -rotate forward,backward
       
       Some variables that need defining:
       - family list
       -
    '''

    def __init__(self,**kwargs):
        kwargs["name"] = "root"
        super().__init__(**kwargs)
        kwargs.pop("name",None)
        self._init_wheel(**kwargs)
        
    def _init_wheel(self,**kwargs):
        self.spokes     =   []
        controller      =   kwargs["controller"]
        spoke_dict      =   self.controller.get_spoke_dict_list()
        divs            =   len(spoke_dict)
        delta_theta     =   360/divs
        spoke_dict      =   self.controller.get_spoke_dict_list()
        for i in range(0,divs):
            start_angle = i*delta_theta
            spoke       = Spoke(angle=start_angle,delta_theta=delta_theta,controller=controller,**spoke_dict[i])
            self.spokes.append(spoke)
            print(spoke.toString())
            
    def rotate(self,angle):
        self._rotate(angle)
        for spoke in self.spokes:
            spoke.rotate(angle)
    
class Spoke(Widget,AbstractSpoke):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self._init_self_properties(**kwargs)
        self._init_children(**kwargs)
        
    def _init_self_properties(self,**kwargs):
        self.angle          = kwargs["angle"]
        self.delta_theta    = kwargs["delta_theta"]
        
    def rotate(self,angle):
        self._rotate(angle)
        
    def toString(self):
        output = "angle:" + str(self.angle) + " dtheta:" + str(self.delta_theta) + " name:" + str(self.name)
        return output