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

    # body element
    body = widget.newFrame(dashboard.window, "#202020", 0)
    body.pack(expand=True, fill="both")

    # sidebar
    sidebar = widget.newFrame(body, "transparent", 0, 200)
    sidebar.pack(side="left", fill="y", padx=10)

    # sidebar menus
    home = widget.newFrame(sidebar, "white", 0, "", 50)
    home.pack(side="top", expand=True, fill="x")

    # content element
    content = widget.newFrame(body, "transparent", 0)
    content.pack(side="left", expand=True, fill="both")

    # button = widget.newButton(body, "test", button_function)
    # button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    dashboard.openMaximised()

if __name__ == '__main__':
    dashboardUi()
