'''
Created on Oct 9, 2017

@author: kevinmendoza
'''
from root.gui.gui_main                  import GuiMain
from root.controller.controller_main    import ControllerMain
from root.data_base.data_main           import DataBase
if __name__ == '__main__':
    controller  = ControllerMain()
    guiMain     = GuiMain(controller)
    dataBase    = DataBase(controller)