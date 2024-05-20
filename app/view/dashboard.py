import customtkinter as ctk
from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name

path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget

def button_function():
    print("button pressed")

def home_page(widget, content):
    home_container = widget.new_frame(content, "transparent", 5)
    home_container.pack(expand=True, fill="both", padx=10, pady=10)

    input = widget.new_input(home_container, "#323232")
    input.pack(fill="x", pady=(12,0), padx=27, ipady=10)

def menu_page(widget, content):
    label = widget.new_label(content, "Menu")
    label.pack(expand=True)

def settings_page(widget, content):
    label = widget.new_label(content, "Settings")
    label.pack(expand=True)

def about_page(widget, content):
    label = widget.new_label(content, "About")
    label.pack(expand=True)

def set_frame_focus(frames, frame_to_focus):
    for frame in frames:
        if frame == frame_to_focus:
            frame.set_focus()
        else:
            frame.clear_focus()

def create_sidebar_frame(widget, parent, text, frames, content, click_function=None):
    frame = widget.new_frame(parent, "transparent", 5, None, 50)
    frame.set_focus_color("#2b2b2b")
    frame.pack_propagate(False)
    frame.pack(side="top", fill="x", pady=5)
    frame.on_hover("#323232")
    frame.on_click(lambda: (
        widget.clear_widget(content),
        click_function(widget, content)
        if click_function else None,
        set_frame_focus(frames, frame))
    )
    label = widget.new_label(frame, text)
    label.pack(pady=10, anchor="center")
    return frame

def dashboard_ui():
    dashboard = CtkWindow("Dashboard")
    widget = CtkWidget()
    frames = []

    # Body element
    body = widget.new_frame(dashboard.window, "#121212", 0)
    body.pack(expand=True, fill="both")

    # Sidebar
    sidebar = widget.new_frame(body, "transparent", 0, 200)
    sidebar.pack(side="left", fill="y", padx=15, pady=10)

    # Content element
    main_container = widget.new_frame(body, "transparent", 0)
    main_container.pack(side="left", expand=True, fill="both", pady=(15, 10), padx=(0,10))

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
        frame = create_sidebar_frame(
            widget, sidebar, label, frames, content,
            click_function=function
        )
        frames.append(frame)

    # Focus the "Home" frame
    set_frame_focus(frames, frames[0])
    home_page(widget, content)

    dashboard.open_maximised()

if __name__ == '__main__':
    dashboard_ui()
