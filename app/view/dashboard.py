import customtkinter
from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name
path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget

def button_function():
    print("button pressed")

def home_function():
    print("home")

def set_frame_focus(frames, frame_to_focus):
    for frame in frames:
        if frame == frame_to_focus:
            frame.set_focus()
        else:
            frame.clear_focus()

def create_sidebar_frame(widget, parent, text, frames, click_function=None):
    frame = widget.new_frame(parent, "black", 5, None, 50)
    frame.pack_propagate(False)
    frame.pack(side="top", fill="x", pady=5)
    frame.on_hover("white")
    frame.on_click(
        lambda: (
            click_function() if click_function
            else None, set_frame_focus(frames, frame)
        )
    )
    label = widget.new_label(frame, text)
    label.pack(pady=10, anchor="center")
    return frame

def dashboard_ui():
    dashboard = CtkWindow("Dashboard")
    widget = CtkWidget()
    frames = []

    # body element
    body = widget.new_frame(dashboard.window, "#202020", 0)
    body.pack(expand=True, fill="both")

    # sidebar
    sidebar = widget.new_frame(body, "transparent", 0, 200)
    sidebar.pack(side="left", fill="y", padx=15, pady=10)

    # List of menu items and corresponding functions
    menu_items = [
        ("Home", home_function),
        ("Menu", None),
        ("Home", None),
        ("Menu", None),
        ("Home", None),
        ("Menu", None),
        ("Home", None),
        ("Menu", None),
    ]

    for label, function in menu_items:
        frame = create_sidebar_frame(
            widget, sidebar, label, frames, click_function=function
        )
        frames.append(frame)

    # content element
    content = widget.new_frame(body, "transparent", 0)
    content.pack(side="left", expand=True, fill="both", pady=(15, 10), padx=(0,10))

    content_body = widget.new_frame(content, "black", 5)
    content_body.pack(expand=True, fill="both")

    button = widget.new_button(content_body, "test", button_function)
    button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    dashboard.open_maximised()

if __name__ == '__main__':
    dashboard_ui()
