import customtkinter
from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name
path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget

def button_function():
    print("button pressed")

def home_function(home):
    home.set_focus()
    print("home clicked")

def dashboard_ui():
    dashboard = CtkWindow("Dashboard")
    widget = CtkWidget()

    # body element
    body = widget.new_frame(dashboard.window, "#202020", 0)
    body.pack(expand=True, fill="both")

    # sidebar
    sidebar = widget.new_frame(body, "transparent", 0, 200)
    sidebar.pack(side="left", fill="y", padx=15, pady=10)

    # sidebar menus
    home = widget.new_frame(sidebar, "black", 5, None, 50)
    home.pack_propagate(False)
    home.pack(side="top", fill="x", pady=(0,5))
    home.on_hover("white")
    home.on_click(lambda: home_function(home))

    home_label = widget.new_label(home, "Home")
    home_label.pack(pady=10, anchor="center")

    menu = widget.new_frame(sidebar, "black", 5, None, 50)
    menu.pack(side="top", fill="x", pady=5)
    menu.on_hover("white")

    home2 = widget.new_frame(sidebar, "black", 5, None, 50)
    home2.pack(side="top", fill="x", pady=5)
    home2.on_hover("white")

    menu2 = widget.new_frame(sidebar, "black", 5, None, 50)
    menu2.pack(side="top", fill="x", pady=5)
    menu2.on_hover("white")

    home3 = widget.new_frame(sidebar, "black", 5, None, 50)
    home3.pack(side="top", fill="x", pady=5)
    home3.on_hover("white")

    menu3 = widget.new_frame(sidebar, "black", 5, None, 50)
    menu3.pack(side="top", fill="x", pady=5)
    menu3.on_hover("white")

    home4 = widget.new_frame(sidebar, "black", 5, None, 50)
    home4.pack(side="top", fill="x", pady=5)
    home4.on_hover("white")

    menu4 = widget.new_frame(sidebar, "black", 5, None, 50)
    menu4.pack(side="top", fill="x", pady=5)
    menu4.on_hover("white")

    # content element
    content = widget.new_frame(body, "transparent", 0)
    content.pack(side="left", expand=True, fill="both", pady=(10, 10), padx=(0,10))

    content_body = widget.new_frame(content, "black", 5)
    content_body.pack(expand=True, fill="both")

    button = widget.new_button(content_body, "test", button_function)
    button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    dashboard.open_maximised()

if __name__ == '__main__':
    dashboard_ui()
