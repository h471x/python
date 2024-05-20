import customtkinter as ctk
from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name

path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget

def close_window(window):
    return lambda: (
        window.close()
    )

def home_page(dashboard, widget, content):
    home_container = widget.new_frame(content, "transparent", 5)
    home_container.pack(expand=True, fill="both", padx=10, pady=10)

    input = widget.new_input(home_container, "#323232")
    input.pack(fill="x", pady=(12,0), padx=27, ipady=10)

def menu_page(dashboard, widget, content):
    button = widget.new_button(content, "Close", close_window(dashboard))
    button.pack(expand=True)

def settings_page(dashboard, widget, content):
    label = widget.new_label(content, "Settings")
    label.pack(expand=True)

def about_page(dashboard, widget, content):
    label = widget.new_label(content, "About")
    label.pack(expand=True)

def set_button_focus(buttons, button_to_focus):
    for button in buttons:
        if button == button_to_focus:
            button.set_focus()
        else:
            button.clear_focus()

def create_sidebar_button(
    widget, parent, text, buttons, content,
    width, height, color, hover, focus,
    dashboard, click_function=None ):
    button = widget.new_button(
        parent, text,
        lambda: (
            widget.clear_widget(content),
            click_function(dashboard, widget, content) if click_function else None,
            set_button_focus(buttons, button)
        ),
        color, width, height, 5, hover, focus
    )
    button.pack_propagate(False)
    button.pack(side="top", fill="x", pady=5)
    return button

def dashboard_ui():
    dashboard = CtkWindow("Dashboard")
    widget = CtkWidget()
    buttons = []

    # Body element
    body = widget.new_frame(dashboard.window, "#121212", 0)
    body.pack(expand=True, fill="both")

    # Sidebar
    sidebar = widget.new_frame(body, "transparent", 0, 200)
    sidebar.pack(side="left", fill="y", padx=15, pady=10)

    # Content element
    main_container = widget.new_frame(body, "transparent", 0)
    main_container.pack(
        side="left", expand=True, fill="both", pady=(15, 10), padx=(0,10)
    )

    content = widget.new_frame(main_container, "#262626", 5)
    content.pack(expand=True, fill="both")

    # List of menu items and corresponding functions
    menu_items = [
        ("Home", home_page),
        ("Menu", menu_page),
        ("Settings", settings_page),
        ("About", about_page),
    ]

    for label, function in menu_items:
        button = create_sidebar_button(
            widget, sidebar, label, buttons, content,
            200, 50, "#121212", "#323232", "#2b2b2b",
            dashboard, click_function=function
        )
        buttons.append(button)

    # Focus the "Home" button
    set_button_focus(buttons, buttons[0])
    home_page(dashboard, widget, content)

    dashboard.open_maximised()

if __name__ == '__main__':
    dashboard_ui()
