import customtkinter as ctk
from customtkinter import *

import tkinter as tk
from tkinter import ttk

from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name

path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget

from app.controllers.admin import *
from app.controllers.student import *
from app.controllers.teacher import *

from assets.styles.colors import *
from assets.styles.dimensions import *
from assets.styles.defaults import configure_table_styles

def close_window(window):
    return lambda: (
        window.close()
    )

def dashboard_page(dashboard, widget, content):
    home_container = widget.new_frame(content, "transparent", 5)
    home_container.pack(expand=True, fill="both", padx=10, pady=10)

    users = student.raw_get(f"""
        SELECT last_name FROM admin;
    """)

    users_list = widget.new_dropdown(
        home_container,
        [user[0] for user in users],
        125, 30, "center"
    ).pack(
        side="top",
        padx=(13, 0),
        pady=15,
        expand=True
    )

    input = widget.new_input(home_container, "#323232")
    input.pack(fill="x", pady=(12,0), padx=27, ipady=10, ipadx=30)

    # label = widget.new_label(home_container, "Dashboard")
    # label.pack(expand=True)

def classes_page(dashboard, widget, content):
    label = widget.new_label(content, "Classes")
    label.pack(expand=True)

def teacher_page(dashboard, widget, content):
    label = widget.new_label(content, "Teachers")
    label.pack(expand=True)

def student_page(dashboard, widget, content):
    student_container = widget.new_frame(content, "transparent", 5)
    student_container.pack(expand=True, fill="both", padx=10, pady=10)

    table_data = admin.raw_get(f"""
        SELECT
            id_card as IdCard,
            first_name as FirstName,
            last_name as LastName,
            birth as DoB,
            phone as Phone
        FROM admin
    """)

    # Extract the header row from `table_data`
    header_row = table_data[0]
    body_data = table_data[1:]

    # Create a frame to hold the table and the header
    table_frame = widget.new_frame(student_container, "transparent", 5)
    table_frame.pack(side="left", expand=True, fill="both", padx=0, pady=0)

    # Call the styles
    configure_table_styles(dashboard.window)

    # Create a frame for the headers inside the table frame
    header_frame = widget.new_frame(table_frame, "transparent", 5)
    header_frame.pack(fill="x", padx=0, pady=0)

    # Create the Treeview for headers only
    header_tree = ttk.Treeview(header_frame, columns=header_row, show="headings", height=0, style="Treeview")
    header_tree.pack(fill="x", padx=0, pady=0)

    for col in header_row:
        header_tree.heading(col, text=col, anchor=tk.CENTER)
        header_tree.column(col, anchor=tk.CENTER, stretch=True)

    # Create the Treeview
    columns = header_row
    tree = ttk.Treeview(
        table_frame, columns=columns, show="", style="Treeview"
    )
    tree.pack(expand=True, fill="both")

    # Create a new frame to hold the table_frame and the scrollbar
    outer_frame = widget.new_frame(student_container, "transparent", 5)
    outer_frame.pack(expand=True, fill="both", padx=0, pady=0)

    # Place the table frame inside the outer frame
    table_frame.pack(side="left", expand=True, fill="both")

    # Create and place the scrollbar outside the table frame on the right
    scrollbar = ctk.CTkScrollbar(
        outer_frame, orientation="vertical", command=tree.yview
    )
    scrollbar.pack(side="right", fill="y")

    tree.configure(yscrollcommand=scrollbar.set)

    for col in columns:
        tree.column(col, anchor=tk.CENTER, stretch=True)

    tag_count = 0
    for row in body_data:
        tag = "row2" if tag_count % 2 else "row1"
        tree.insert("", tk.END, values=row, tags=(tag,))
        tag_count += 1

    tree.tag_configure("row1", background=row1_color)
    tree.tag_configure("row2", background=row2_color)

    def adjust_column_widths(tree, header_tree, columns):
        for col in columns:
            max_len = len(col)
            for item in tree.get_children():
                text = str(tree.item(item, "values")[columns.index(col)])
                max_len = max(max_len, len(text))
            width = max_len * 10
            tree.column(col, width=width)
            header_tree.column(col, width=width)

    adjust_column_widths(tree, header_tree, columns)

def settings_page(dashboard, widget, content):
    label = widget.new_label(content, "Settings")
    label.pack(expand=True)

def about_page(dashboard, widget, content):
    # image_path = "assets/python.png"
    # image = widget.new_image(content, image_path, width=200, height=200)
    # image.pack(pady=50)
    label = widget.new_label(content, "About")
    label.pack(expand=True)

    button = widget.new_button(
        content, "Close", close_window(dashboard)
    )
    button.pack(expand=True)

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
    dashboard = CtkWindow("e-school")
    dashboard.set_size(990,500)
    widget = CtkWidget()
    buttons = []

    # Body element
    body = widget.new_frame(dashboard.window, body_bg_color, 0)
    body.pack(expand=True, fill="both")
 
    # Sidebar
    sidebar = widget.new_frame(body, "transparent", 0, sidebar_width)
    sidebar.pack(side="left", fill="y", padx=15, pady=10)

    # Content element
    main_container = widget.new_frame(body, "transparent", 0)
    main_container.pack(
        side="left", expand=True, fill="both", pady=(10, 10), padx=(0,10)
    )

    content = widget.new_frame(main_container, content_bg_color, 5)
    content.pack(expand=True, fill="both")

    # List of menu items and corresponding functions
    menu_items = [
        ("Dashboard", dashboard_page),
        ("Classes", classes_page),
        ("Teachers", teacher_page),
        ("Students", student_page),
        ("Settings", settings_page),
        ("About", about_page),
    ]

    for label, function in menu_items:
        button = create_sidebar_button(
            widget, sidebar, label, buttons, content,
            sidebar_width, sidebar_height,
            sidebar_color, sidebar_hover_color, sidebar_focus_color,
            dashboard, click_function=function
        )
        buttons.append(button)

    # Focus the "Home" button
    set_button_focus(buttons, buttons[0])
    dashboard_page(dashboard, widget, content)

    dashboard.open_maximised()

if __name__ == '__main__':
    dashboard_ui()
