#!/usr/bin/python
from config.database.connect import getStatus, initTables

from app.view.dashboard import dashboardUi
from app.view.qtlogin import LoginUi
from classes.window.qtwindow import QtWindow, GuiApp

def openLogin():
    login = QtWindow(LoginUi(), GuiApp)
    login.open()

if __name__ == '__main__':
    if getStatus() == 'connected':
        if initTables():
            # openLogin()
            dashboardUi()
