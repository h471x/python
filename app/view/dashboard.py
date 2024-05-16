import customtkinter
from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget

def button_function():
    print("button pressed")

def dashboardUi():
    dashboard = CtkWindow("Dashboard")
    widget = CtkWidget()

    button = widget.newButton(
        dashboard.window,
        "test",
        button_function
    )
    button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
    # frame = widget.newFrame(
    #     dashboard.window,
    #     "blue",
    #     0
    # )
    dashboard.openMaximised()

if __name__ == '__main__':
    dashboardUi()
