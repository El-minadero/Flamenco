'''
Created on Oct 9, 2017

@author: kevinmendoza
'''

class ControllerMain(object):
    def __init(self,controller):
        pass 
    
    def get_spoke_dict_list(self):
        spoke_dict_list = []
        d1              = {}
        d1["name"]      = "first"
        d1["children"]  = ["one","two","three"]
        d2              = {}
        d2["name"]      = "second"
        d2["children"]  = ["i","ii","iii"]
        d3              = {}
        d3["name"]      = "third"
        d3["children"]  = ["ichi","knee","san"]
        
        spoke_dict_list.append(d1)
        spoke_dict_list.append(d2)
        spoke_dict_list.append(d3)
        return spoke_dict_list
        
        
