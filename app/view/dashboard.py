import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import ttk
from CTkTable import CTkTable
from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name

path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget
from app.controllers.student import *
from assets.styles.defaults import configure_styles

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

    # get data from database
    # table_data = student_select_all()
    table_data = student.raw_get(f"""
        SELECT
            student_id AS IdNum,
            last_name as LastName,
            first_name as FirstName,
            major as Grade,
            level as Level,
            phone as PhoneNumber,
            adress as Adress
        FROM student
    """)

    # Create a scrollable frame for the table body
    table_frame = CTkFrame(master=home_container, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=(21,0), pady=0)

    # Extract the header row from `table_data`
    header_row = table_data[0]
    body_data = table_data[1:]

    # Apply styles
    configure_styles()

    # Create the Treeview
    columns = header_row
    tree = ttk.Treeview(
        table_frame, columns=columns, show="headings", style="Treeview"
    )

    # Define headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER, stretch=True)

    # Insert data
    # for row in body_data:
    #     tree.insert("", tk.END, values=row)

    tag_count = 0
    for row in body_data:
        tag = 'row1' if tag_count % 2 == 0 else 'row2'
        tree.insert("", tk.END, values=row, tags=(tag,))
        tag_count += 1

    # Apply the tags to the rows
    tree.tag_configure('row1', background='#363636')
    tree.tag_configure('row2', background='#282828')

    # Adjust column widths based on content
    def adjust_column_widths(tree, columns):
        for col in columns:
            max_len = len(col)
            for item in tree.get_children():
                text = str(tree.item(item, "values")[columns.index(col)])
                max_len = max(max_len, len(text))
            tree.column(col, width=max_len * 10)

    adjust_column_widths(tree, columns)

    # Create a scrollbar for the Treeview
    scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tree.pack(expand=True, fill='both', pady=20)

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

    # Width of the sidebar
    sidebar_width = 100

    # Sidebar
    sidebar = widget.new_frame(body, "transparent", 0, sidebar_width)
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
            sidebar_width, 50, "#121212", "#323232", "#2b2b2b",
            dashboard, click_function=function
        )
        buttons.append(button)

    # Focus the "Home" button
    set_button_focus(buttons, buttons[0])
    home_page(dashboard, widget, content)

    dashboard.open_maximised()

if __name__ == '__main__':
    dashboard_ui()
