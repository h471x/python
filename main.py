from config.database.connect import getStatus
from config.database.init import initDbTable

from app.view.gui import mainGui
from app.view.login import LoginUi
from classes.qtwindow import QtWindow, GuiApp

def openLogin():
    login = QtWindow(LoginUi(), GuiApp)
    login.open()

if __name__ == '__main__':
    # mainGui() if getStatus() == 'connected' else None
    # openLogin() if getStatus() == 'connected' else None
    initDbTable() if getStatus() == 'connected' else None
