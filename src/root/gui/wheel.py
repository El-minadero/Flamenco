'''
Created on Oct 18, 2017

@author: kevinmendoza
'''
from kivy.uix.widget import Widget

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