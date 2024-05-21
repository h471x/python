#!/usr/bin/python
from config.database.connect import get_status, init_tables

from app.view.dashboard import dashboard_ui
from app.view.qtlogin import LoginUi
from classes.window.pyqt6.qtwindow import QtWindow, GuiApp

def open_login():
    login = QtWindow(LoginUi(), GuiApp)
    login.open()

debug_mode = True

if __name__ == '__main__':
    if debug_mode:
        dashboard_ui()
    else:
        if get_status() == 'connected':
            if init_tables():
                # open_login()
                dashboard_ui()
