import customtkinter
from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow

def dashboardUi():
    dashboard = CtkWindow("Dashboard")

    def button_function():
        print("button pressed")

    # Use CTkButton instead of tkinter Button
    button = customtkinter.CTkButton(master=dashboard.getWindow(), text="CTkButton", command=button_function)
    button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    dashboard.openMaximised()

if __name__ == '__main__':
    dashboardUi()
