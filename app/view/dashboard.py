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
from app.controllers.grade import *
from app.controllers.ce import *

from assets.styles.colors import Common as common
from assets.styles.colors import Dashboard as dash
from assets.styles.colors import Treeview as treeView

from assets.styles.dimensions import *
from assets.styles.defaults import configure_table_styles

def close_window(window):
    return lambda: (
        window.close()
    )

def setup_treeview(tree, columns, body_data):
    # Clear existing items in the treeview
    tree.delete(*tree.get_children())

    # Insert new data into the treeview
    tag_count = 0
    for row in body_data:
        tag = "row2" if tag_count % 2 else "row1"
        tree.insert("", tk.END, values=row, tags=(tag,))
        tag_count += 1

    # Configure tags for alternating row colors
    tree.tag_configure("row1", background=treeView.row1_color)
    tree.tag_configure("row2", background=treeView.row2_color)

def create_card(widget, parent, text, color, width, height, number):
    card = widget.new_frame(parent, color, 5)
    card.pack_propagate(False)  # Prevent the frame from resizing to fit the content

    content_frame = widget.new_frame(card, color, 0)
    content_frame.pack(expand=True, fill="both", padx=10, pady=10)  # Adjust padding as needed

    label_frame = widget.new_frame(content_frame, color, 0)
    label_frame.pack(expand=True, fill="both")

    label = widget.new_label(label_frame, text)
    label.pack(expand=True)

    number_frame = widget.new_frame(content_frame, color, 0)
    number_frame.pack(expand=True, fill="both")

    number_label = widget.new_label(number_frame, str(number))
    number_label.pack(expand=True)

    card.configure(width=width, height=height)
    return card

def dashboard_page(dashboard, widget, content):
    home_container = widget.new_frame(content, "transparent", 5)
    home_container.pack(expand=True, fill="both", padx=10, pady=10)

    # Create a 2x2 grid for cards
    card_width = 200
    card_height = 150

    card_labels = [
        "Classes",
        "Teachers",
        "Students"
    ]

    card_colors = [
        common.pink_color,
        common.green_color,
        common.blue2_color
    ]

    card_numbers = [
        ce_count(),
        teacher_count(),
        student_count()
    ]

    for i in range(2):
        for j in range(2):
            index = i*2 + j
            if index < len(card_labels):
                card_text = card_labels[index]
                card_color = card_colors[index]
                card_number = card_numbers[index]
                create_card(
                    widget, home_container, card_text,
                    card_color, card_width, card_height, card_number
                ).grid(row=i, column=j, padx=10, pady=10, sticky="nsew")
            else:
                break

    # Configure the grid to expand correctly
    for i in range(2):
        home_container.grid_rowconfigure(i, weight=1)
    for j in range(2):
        home_container.grid_columnconfigure(j, weight=1)    # users = student.raw_get(f"""
    #     SELECT last_name FROM admin;
    # """)
    #
    # users_list = widget.new_dropdown(
    #     home_container,
    #     [user[0] for user in users],
    #     125, 30, "center"
    # ).pack(
    #     side="top",
    #     padx=(13, 0),
    #     pady=15,
    #     expand=True
    # )
    #
    # input = widget.new_input(home_container, common.input_bg_color)
    # input.pack(fill="x", pady=(12,0), padx=27, ipady=10, ipadx=30)
    #
    # label = widget.new_label(home_container, "Dashboard")
    # label.pack(expand=True)

def classes_page(dashboard, widget, content):
    student_container = widget.new_frame(content, "transparent", 5)
    student_container.pack(expand=True, fill="both", padx=10, pady=10)

    admins = f"""
        SELECT
            id_card as IdCard,
            first_name as FirstName,
            last_name as LastName,
            birth as DoB,
            phone as Phone,
            gender as Gender
        FROM admin
    """

    table_data = admin.raw_get(admins)

    # Extract the header row from `table_data`
    header_row = list(table_data[0]) + ["Edit", "Delete"]
    body_data = [list(row) + ["Edit", "Delete"] for row in table_data[1:]]

    # Create a frame to hold the table and the header
    table_frame = widget.new_frame(student_container, "transparent", 5)
    table_frame.pack(side="left", expand=True, fill="both", padx=0, pady=0)

    # Call the styles
    configure_table_styles(dashboard.window)

    # Create a frame for the headers inside the table frame
    header_frame = widget.new_frame(table_frame, "transparent", 5)
    header_frame.pack(fill="x", padx=0, pady=0)

    # Create the Treeview for headers only
    header_tree = ttk.Treeview(
        header_frame, columns=header_row,
        show="headings", height=0, style="Treeview"
    )
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

    # Initial setup of treeview with data
    setup_treeview(tree, columns, body_data)

    def on_action_click(event):
        item = tree.identify_row(event.y)
        if item:
            tree.focus(item)  # Set focus on the clicked item
            tree.selection_set(item)  # Select the clicked item
            column = tree.identify_column(event.x)
            id_card = tree.item(item, 'values')[0]

            if column == '#%d' % (len(columns) - 1):  # Edit column
                print(f"Edit action for ID Card: {id_card}")
                edit_student = CtkWindow("Edit Student")
                edit_student.set_size(750,600)

                # To center header frame
                edit_student.window.grid_columnconfigure(0,weight=1)
                edit_student.window.grid_columnconfigure(1,weight=1)

                edit_student.window.grid_rowconfigure(0,weight=1)
                edit_student.window.grid_rowconfigure(1,weight=1)
                edit_student.window.grid_rowconfigure(2,weight=1)
                # first frame for the header
                header = widget.new_frame(edit_student.window,common.blue_color,5)
                header.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="ew")

                # Center label in header
                header.grid_columnconfigure(0,weight=1)
                edit_student_label = widget.new_label(header,"Modification",font=("Roboto",40))

                edit_student_label.grid(row=0,column=0,columnspan=2, padx=10, pady=10,sticky="ew")
                # second frame for body1 that contains the input widgets
                body = widget.new_frame(edit_student.window,"transparent",5)
                body.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

                # First name
                body1 = widget.new_frame(body,"transparent",5)
                body2 = widget.new_frame(body,"transparent",5)

                # body1.pack(expand=True, fill="both", padx=10, pady=10)
                body1.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
                body2.grid(row=1,column=1,padx=10,pady=10,sticky="nsew")

                firstname_label = widget.new_label(body1,"First Name",font=("Roboto",20))
                firstname_label.grid(row=0,column=0,padx=10,pady=10)

                firstname_input = widget.new_input(body1,common.input_bg_color,placeholder_text="First Name",font=("Roboto",15),corner_radius=10)
                firstname_input.configure(font=("Roboto", 16), height=40, width=200)
                firstname_input.grid(row=0,column=1,padx=10,pady=10)


                edit_student.always_on_top()
                edit_student.open_centered()

            # Implement your edit logic here
            elif column == '#%d' % len(columns):  # Delete column
                print(f"Delete action for ID Card: {id_card}")
                delete_student = CtkWindow("Delete Student")
                delete_student.set_size(400, 200)
                delete_student.always_on_top()
                delete_student.not_resizable()

                # Function to handle the Confirm button action
                def confirm_action(delete_student, delete_widget, tree):
                    # Clear the content of the delete_student window
                    for widget in delete_student.window.winfo_children():
                        widget.pack_forget()

                    # Add the "Deleted Successfully" label
                    success_label = delete_widget.new_label(
                        delete_student.window,
                        "Deleted Successfully"
                    )
                    success_label.configure(font=('Roboto', 22, "bold"))
                    success_label.pack(pady=(10, 20))

                    # Add the ID card label
                    id_card_label = delete_widget.new_label(delete_student.window, id_card)
                    id_card_label.pack(pady=(0, 20))

                    def confirm_delete(tree, columns):
                        admin_delete({'id_card' : id_card})
                        new_body_data = [
                            list(row) + ["Edit", "Delete"]
                            for row in admin.raw_get(admins)[1:]
                        ]
                        setup_treeview(tree, columns, new_body_data)
                        delete_student.close()

                    delete_student.window.after(
                        500,
                        lambda : confirm_delete(
                            tree, columns
                        )
                    )

                    # Add your logic for confirm action here
                    print("Confirm button clicked")

                # Function to handle the Cancel button action
                def cancel_action(delete_student):
                    # Add your logic for cancel action here
                    delete_student.close()
                    print("Cancel button clicked")

                # Add the "Confirm Deletion?" label
                confirm_label = widget.new_label(delete_student.window, "Confirm Deletion ?")
                confirm_label.configure(font=('Roboto', 15, "bold"))
                confirm_label.pack(pady=(20, 10))

                # Add the ID card label
                id_card_label = widget.new_label(delete_student.window, id_card)
                id_card_label.pack(pady=(0, 20))

                # Frame to hold the buttons
                confirm_cancel_frame = widget.new_frame(delete_student.window, "transparent", 5)
                confirm_cancel_frame.pack(pady=(30, 30), padx=10, fill="x")

                confirm_button = widget.new_button(
                    confirm_cancel_frame,
                    "Delete",
                    lambda : confirm_action(
                        delete_student, widget, tree
                    ),
                    "#c42b1c"
                )
                confirm_button.pack(side="left", padx=30)

                delete_button = widget.new_button(
                    confirm_cancel_frame, "Cancel", lambda : cancel_action(delete_student),
                    "#323232"
                )
                delete_button.pack(side="right", padx=30)

                delete_student.open_centered()
    tree.bind("<ButtonRelease-1>", on_action_click)

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

def teacher_page(dashboard, widget, content):
    student_container = widget.new_frame(content, "transparent", 5)
    student_container.pack(expand=True, fill="both", padx=10, pady=10)

    admins = f"""
        SELECT
            id_card as IdCard,
            first_name as FirstName,
            last_name as LastName,
            birth as DoB,
            phone as Phone,
            gender as Gender
        FROM admin
    """

    table_data = admin.raw_get(admins)

    # Extract the header row from `table_data`
    header_row = list(table_data[0]) + ["Edit", "Delete"]
    body_data = [list(row) + ["Edit", "Delete"] for row in table_data[1:]]

    # Create a frame to hold the table and the header
    table_frame = widget.new_frame(student_container, "transparent", 5)
    table_frame.pack(side="left", expand=True, fill="both", padx=0, pady=0)

    # Call the styles
    configure_table_styles(dashboard.window)

    # Create a frame for the headers inside the table frame
    header_frame = widget.new_frame(table_frame, "transparent", 5)
    header_frame.pack(fill="x", padx=0, pady=0)

    # Create the Treeview for headers only
    header_tree = ttk.Treeview(
        header_frame, columns=header_row,
        show="headings", height=0, style="Treeview"
    )
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

    # Initial setup of treeview with data
    setup_treeview(tree, columns, body_data)

    def on_action_click(event):
        item = tree.identify_row(event.y)
        if item:
            tree.focus(item)  # Set focus on the clicked item
            tree.selection_set(item)  # Select the clicked item
            column = tree.identify_column(event.x)
            id_card = tree.item(item, 'values')[0]

            if column == '#%d' % (len(columns) - 1):  # Edit column
                print(f"Edit action for ID Card: {id_card}")
                edit_student = CtkWindow("Edit Student")
                edit_student.set_size(750,600)

                # To center header frame
                edit_student.window.grid_columnconfigure(0,weight=1)
                edit_student.window.grid_columnconfigure(1,weight=1)

                edit_student.window.grid_rowconfigure(0,weight=1)
                edit_student.window.grid_rowconfigure(1,weight=1)
                edit_student.window.grid_rowconfigure(2,weight=1)
                # first frame for the header
                header = widget.new_frame(edit_student.window,common.blue_color,5)
                header.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="ew")

                # Center label in header
                header.grid_columnconfigure(0,weight=1)
                edit_student_label = widget.new_label(header,"Modification",font=("Roboto",40))

                edit_student_label.grid(row=0,column=0,columnspan=2, padx=10, pady=10,sticky="ew")
                # second frame for body1 that contains the input widgets
                body = widget.new_frame(edit_student.window,"transparent",5)
                body.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

                # First name
                body1 = widget.new_frame(body,"transparent",5)
                body2 = widget.new_frame(body,"transparent",5)

                # body1.pack(expand=True, fill="both", padx=10, pady=10)
                body1.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
                body2.grid(row=1,column=1,padx=10,pady=10,sticky="nsew")

                firstname_label = widget.new_label(body1,"First Name",font=("Roboto",20))
                firstname_label.grid(row=0,column=0,padx=10,pady=10)

                firstname_input = widget.new_input(body1,common.input_bg_color,placeholder_text="First Name",font=("Roboto",15),corner_radius=10)
                firstname_input.configure(font=("Roboto", 16), height=40, width=200)
                firstname_input.grid(row=0,column=1,padx=10,pady=10)


                edit_student.always_on_top()
                edit_student.open_centered()

            # Implement your edit logic here
            elif column == '#%d' % len(columns):  # Delete column
                print(f"Delete action for ID Card: {id_card}")
                delete_student = CtkWindow("Delete Student")
                delete_student.set_size(400, 200)
                delete_student.always_on_top()
                delete_student.not_resizable()

                # Function to handle the Confirm button action
                def confirm_action(delete_student, delete_widget, tree):
                    # Clear the content of the delete_student window
                    for widget in delete_student.window.winfo_children():
                        widget.pack_forget()

                    # Add the "Deleted Successfully" label
                    success_label = delete_widget.new_label(
                        delete_student.window,
                        "Deleted Successfully"
                    )
                    success_label.configure(font=('Roboto', 22, "bold"))
                    success_label.pack(pady=(10, 20))

                    # Add the ID card label
                    id_card_label = delete_widget.new_label(delete_student.window, id_card)
                    id_card_label.pack(pady=(0, 20))

                    def confirm_delete(tree, columns):
                        admin_delete({'id_card' : id_card})
                        new_body_data = [
                            list(row) + ["Edit", "Delete"]
                            for row in admin.raw_get(admins)[1:]
                        ]
                        setup_treeview(tree, columns, new_body_data)
                        delete_student.close()

                    delete_student.window.after(
                        500,
                        lambda : confirm_delete(
                            tree, columns
                        )
                    )

                    # Add your logic for confirm action here
                    print("Confirm button clicked")

                # Function to handle the Cancel button action
                def cancel_action(delete_student):
                    # Add your logic for cancel action here
                    delete_student.close()
                    print("Cancel button clicked")

                # Add the "Confirm Deletion?" label
                confirm_label = widget.new_label(delete_student.window, "Confirm Deletion ?")
                confirm_label.configure(font=('Roboto', 15, "bold"))
                confirm_label.pack(pady=(20, 10))

                # Add the ID card label
                id_card_label = widget.new_label(delete_student.window, id_card)
                id_card_label.pack(pady=(0, 20))

                # Frame to hold the buttons
                confirm_cancel_frame = widget.new_frame(delete_student.window, "transparent", 5)
                confirm_cancel_frame.pack(pady=(30, 30), padx=10, fill="x")

                confirm_button = widget.new_button(
                    confirm_cancel_frame,
                    "Delete",
                    lambda : confirm_action(
                        delete_student, widget, tree
                    ),
                    "#c42b1c"
                )
                confirm_button.pack(side="left", padx=30)

                delete_button = widget.new_button(
                    confirm_cancel_frame, "Cancel", lambda : cancel_action(delete_student),
                    "#323232"
                )
                delete_button.pack(side="right", padx=30)

                delete_student.open_centered()
    tree.bind("<ButtonRelease-1>", on_action_click)

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

def student_page(dashboard, widget, content):
    student_container = widget.new_frame(content, "transparent", 5)
    student_container.pack(expand=True, fill="both", padx=10, pady=10)

    # Top container frame with 50px height
    top_container = widget.new_frame(student_container, "lightblue", 5)
    top_container.pack(fill="x", padx=10, pady=10)
    top_container.configure(height=50)  # Set height to 50 pixels

    # Bottom container frame for tree and scrollbar
    bottom_container = widget.new_frame(student_container, "transparent", 5)
    bottom_container.pack(expand=True, fill="both", padx=10, pady=10)

    admins = """
        SELECT
            id_card as IdCard,
            first_name as FirstName,
            last_name as LastName,
            birth as DoB,
            phone as Phone,
            gender as Gender
        FROM admin
    """

    table_data = admin.raw_get(admins)

    # Extract the header row from `table_data`
    header_row = list(table_data[0]) + ["Edit", "Delete"]
    body_data = [list(row) + ["Edit", "Delete"] for row in table_data[1:]]

    # Create a frame to hold the table and the header
    table_frame = widget.new_frame(bottom_container, "transparent", 5)
    table_frame.pack(side="left", expand=True, fill="both")

    # Call the styles
    configure_table_styles(dashboard.window)

    # Create a frame for the headers inside the table frame
    header_frame = widget.new_frame(table_frame, "transparent", 5)
    header_frame.pack(fill="x", padx=0, pady=0)

    # Create the Treeview for headers only
    header_tree = ttk.Treeview(
        header_frame, columns=header_row,
        show="headings", height=0, style="Treeview"
    )
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
    outer_frame = widget.new_frame(bottom_container, "transparent", 5)
    outer_frame.pack(expand=True, fill="both")

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

    # Initial setup of treeview with data
    setup_treeview(tree, columns, body_data)

    def on_action_click(event):
        item = tree.identify_row(event.y)
        if item:
            tree.focus(item)  # Set focus on the clicked item
            tree.selection_set(item)  # Select the clicked item
            column = tree.identify_column(event.x)
            id_card = tree.item(item, 'values')[0]

            if column == '#%d' % (len(columns) - 1):  # Edit column
                print(f"Edit action for ID Card: {id_card}")
                # Implement edit logic here

            elif column == '#%d' % len(columns):  # Delete column
                print(f"Delete action for ID Card: {id_card}")
                # Implement delete logic here

    tree.bind("<ButtonRelease-1>", on_action_click)

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
    body = widget.new_frame(dashboard.window, dash.body_color, 0)
    body.pack(expand=True, fill="both")
 
    # Sidebar
    sidebar = widget.new_frame(body, "transparent", 0, sidebar_width)
    sidebar.pack(side="left", fill="y", padx=15, pady=10)

    # Content element
    main_container = widget.new_frame(body, "transparent", 0)
    main_container.pack(
        side="left", expand=True, fill="both", pady=(10, 10), padx=(0,10)
    )

    content = widget.new_frame(main_container, dash.content_color, 5)
    content.pack(expand=True, fill="both")

    # List of menu items and corresponding functions
    menu_items = [
        ("Dashboard", dashboard_page),
        ("Classes", classes_page),
        ("Teachers", teacher_page),
        ("Students", student_page),
        # ("Settings", settings_page),
        # ("About", about_page),
    ]

    for label, function in menu_items:
        button = create_sidebar_button(
            widget, sidebar, label, buttons, content,
            sidebar_width, sidebar_height,
            dash.sidebar_color, dash.sidebar_hover_color, dash.sidebar_focus_color,
            dashboard, click_function=function
        )
        buttons.append(button)

    # Focus the "Home" button
    set_button_focus(buttons, buttons[0])
    dashboard_page(dashboard, widget, content)

    dashboard.open_maximised()

if __name__ == '__main__':
    dashboard_ui()
