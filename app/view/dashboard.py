import customtkinter as ctk
from customtkinter import *
from CTkTable import CTkTable
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

    # users = ["user1", "user2", "user3"]

    # users_list = widget.new_dropdown(home_container, users, 500, 20)
    # users_list.pack(side="left", padx=(13, 0), pady=15)

    table_data = [
        ["Order ID", "Item Name", "Customer", "Address", "Status", "Quantity"],
        ['3833', 'Smartphone', 'Alice', '123 Main St', 'Confirmed', '8'],
        ['6432', 'Laptop', 'Bob', '456 Elm St', 'Packing', '5'],
        ['2180', 'Tablet', 'Crystal', '789 Oak St', 'Delivered', '1'],
        ['5438', 'Headphones', 'John', '101 Pine St', 'Confirmed', '9'],
        ['9144', 'Camera', 'David', '202 Cedar St', 'Processing', '2'],
        ['7689', 'Printer', 'Alice', '303 Maple St', 'Cancelled', '2'],
        ['1323', 'Smartwatch', 'Crystal', '404 Birch St', 'Shipping', '6'],
        ['7391', 'Keyboard', 'John', '505 Redwood St', 'Cancelled', '10'],
        ['4915', 'Monitor', 'Alice', '606 Fir St', 'Shipping', '6'],
        ['5548', 'External Hard Drive', 'David', '707 Oak St', 'Delivered', '10'],
        ['5485', 'Table Lamp', 'Crystal', '808 Pine St', 'Confirmed', '4'],
        ['7764', 'Desk Chair', 'Bob', '909 Cedar St', 'Processing', '9'],
        ['8252', 'Coffee Maker', 'John', '1010 Elm St', 'Confirmed', '6'],
        ['2377', 'Blender', 'David', '1111 Redwood St', 'Shipping', '2'],
        ['5287', 'Toaster', 'Alice', '1212 Maple St', 'Processing', '1'],
        ['7739', 'Microwave', 'Crystal', '1313 Cedar St', 'Confirmed', '8'],
        ['3129', 'Refrigerator', 'John', '1414 Oak St', 'Processing', '5'],
        ['4789', 'Vacuum Cleaner', 'Bob', '1515 Pine St', 'Cancelled', '10']
    ]

    # Create a frame for the header
    header_frame = CTkFrame(master=home_container, fg_color="transparent")
    header_frame.pack(fill='x', padx=27, pady=(21, 0))  # Padding top only

    # Create a scrollable frame for the table body
    table_frame = CTkScrollableFrame(master=home_container, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=(0, 21))  # Padding bottom only

    # Extract the header row from `table_data`
    header_row = table_data[0]
    body_data = table_data[1:]

    # Create the header table
    header_table = CTkTable(
        master=header_frame, 
        values=[header_row], 
        colors=["#E6E6E6", "#E6E6E6"],  # Ensure two colors are provided
        header_color="#2A8C55", 
        hover_color="#B4B4B4", 
        corner_radius=5
    )
    header_table.edit_row(0, text_color="#000", hover_color="#2A8C55")
    header_table.pack(fill='x')  # Fill horizontally

    # Create the body table
    body_table = CTkTable(
        master=table_frame, 
        values=body_data, 
        colors=["#E6E6E6", "#EEEEEE"],  # Ensure two colors are provided
        header_color="#2A8C55", 
        hover_color="#B4B4B4", 
        corner_radius=5
    )
    body_table.pack(expand=True, fill='both', padx=15, pady=15)

def menu_page(dashboard, widget, content):
    button = widget.new_button(
        content, "Close", close_window(dashboard)
    )
    button.pack(expand=True)

def settings_page(dashboard, widget, content):
    label = widget.new_label(content, "Settings")
    label.pack(expand=True)

def about_page(dashboard, widget, content):
    # label = widget.new_label(content, "About")
    # label.pack(expand=True)

    # image_path = "assets/python.png"
    # image = widget.new_image(content, image_path, width=200, height=200)
    # image.pack(pady=50)
    pass

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
            click_function(dashboard, widget, content)
            if click_function else None,
            set_button_focus(buttons, button)
        ),
        color, width, height, 5, hover, focus
    )
    button.pack_propagate(False)
    button.pack(side="top", fill="x")
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
        side="left", expand=True, fill="both", pady=(10, 10), padx=(0,10)
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
