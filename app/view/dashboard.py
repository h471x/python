from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.window.ctkwindow import CtkWindow

def dashboardUi():
    dashboard = CtkWindow("Dashboard")
    dashboard.openMaximised()

if __name__ == '__main__':
    dashboardUi()
