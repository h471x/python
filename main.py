from config.database.connect import getStatus, initTables

from app.view.gui import mainGui
from app.view.login import LoginUi
from classes.qtwindow import QtWindow, GuiApp

def openLogin():
    login = QtWindow(LoginUi(), GuiApp)
    login.open()

if __name__ == '__main__':
    if getStatus() == 'connected':
        initTables()
        openLogin()
        # mainGui()
