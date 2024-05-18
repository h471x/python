import customtkinter
from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name
path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget

def button_function():
    print("button pressed")

def dashboard_ui():
    dashboard = CtkWindow("Dashboard")
    widget = CtkWidget()

    # body element
    body = widget.new_frame(dashboard.window, "#202020", 0)
    body.pack(expand=True, fill="both")

    # sidebar
    sidebar = widget.new_frame(body, "transparent", 0, 200)
    sidebar.pack(side="left", fill="y", padx=15, pady=20)

    # sidebar menus
    home = widget.new_frame(sidebar, "black", 5, None, 50)
    home.pack(side="top", fill="x")
    home.on_hover("white")

    # content element
    content = widget.new_frame(body, "transparent", 0)
    content.pack(side="left", expand=True, fill="both", pady=(20, 10), padx=(0,10))

    content_body = widget.new_frame(content, "black", 5)
    content_body.pack(expand=True, fill="both")

    button = widget.new_button(content_body, "test", button_function)
    button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    dashboard.open_maximised()

if __name__ == '__main__':
    dashboard_ui()
