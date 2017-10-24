'''
Created on Oct 9, 2017

@author: kevinmendoza
'''
from root.gui.gui_main                  import GuiMainApp
from root.controller.controller_main    import ControllerMain
from root.data_base.data_main           import DataBase

if __name__ == '__main__':
    controller  = ControllerMain()
    guiMain     = GuiMainApp(controller=controller)
    dataBase    = DataBase(controller)
    guiMain.run()