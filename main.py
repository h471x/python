#!/usr/bin/python
from config.database.connect import getStatus, initTables

from app.view.gui import mainGui
from app.view.qtlogin import LoginUi
from classes.utils.qtwindow import QtWindow, GuiApp

def openLogin():
    login = QtWindow(LoginUi(), GuiApp)
    login.open()

if __name__ == '__main__':
    if getStatus() == 'connected':
        if initTables():
            openLogin()
            # mainGui()
