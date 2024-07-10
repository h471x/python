import customtkinter as ctk
from customtkinter import *

import tkinter
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name

path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget
from classes.window.customtkinter.ctkwidget import Notification_frame

from app.controllers.admin import *
from app.controllers.student import *
from app.controllers.teacher import *

from assets.styles.colors import Common as common
from assets.styles.colors import Signup as signupColor
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


    #verification edit student
#Verification fonction
def verification(signup,admin_data,ntfication):
    bval=signup_admin(admin_data, signup)
    ntfication.notif_show(bval)

def show_calendar(event, calendar_view, birth_input):
    # Calculate the position relative to birth_input
    x = birth_input.winfo_rootx()
    y = birth_input.winfo_rooty() + birth_input.winfo_height() + 10

    # Update calendar position
    calendar_view._calendar.winfo_toplevel().geometry(f"+{x}+{y}")

    # Disable direct keyboard input in birth_input
    birth_input.event_generate("<FocusOut>")
    birth_input.event_generate("<Key>")

    # Show the calendar
    calendar_view._calendar.winfo_toplevel().deiconify()

def hide_calendar(event, calendar_view):
    calendar_view._calendar.winfo_toplevel().withdraw()

def calendar_date_selected(event, calendar_view, birth_input, address_input):
    select_date(birth_input, calendar_view, address_input)

# Function to handle date selection
def select_date(entry, date_entry, next_entry):
    selected_date = date_entry.get_date()
    entry.delete(0, tkinter.END)
    entry.insert(0, selected_date)
    next_entry.focus_set()

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

    input = widget.new_input(home_container, common.input_bg_color)
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
                edit_student.set_size(850,600)

                #Begin of form



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

                # focus first_name input on startup
                firstname_input.focus_set()

                # Last name
                lastname_label = widget.new_label(body1,"Last Name",font=("Roboto",20))
                lastname_label.grid(row=1,column=0,padx=10,pady=10,sticky="w")

                lastname_input = widget.new_input(body1,common.input_bg_color,placeholder_text="Last Name",font=("Roboto",15),corner_radius=10)
                lastname_input.configure(font=("Roboto", 16), height=40, width=200)
                lastname_input.grid(row=1,column=1,padx=10,pady=10)

                # Birth
                birth_label = widget.new_label(body1,"Birth Date",font=("Roboto",20))
                birth_label.grid(row=2,column=0,padx=10,pady=10,sticky="w")

                # Calculate the date 18 years ago
                today = datetime.today()
                initial_birth_date = today.replace(year=today.year - 18)

                # Calculate the last date of the previous year
                max_date = datetime(today.year - 1, 12, 31)

                # Birth input
                birth_input = widget.new_input(
                    body1,
                    common.input_bg_color,
                    placeholder_text="Date Of Birth",
                    font=("Roboto",16),
                    corner_radius=10,
                )
                birth_input.configure(height=40, width=200)
                birth_input.grid(row=2,column=1,padx=10,pady=10)

                # Create DateEntry with the calculated initial date and max date
                calendar_view = DateEntry(
                    birth_input,
                    year = initial_birth_date.year,
                    month = initial_birth_date.month,
                    day = initial_birth_date.day,
                    state = "readonly",
                    fieldbackground = 'black',
                    background = common.header_color,
                    foreground = 'white',
                    borderwidth = 2,
                    width = 200,
                    font = calendar_font,
                    maxdate = max_date
                )
                calendar_view.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
             
                # Initially hide the calendar part
                calendar_view._calendar.winfo_toplevel().withdraw()
                calendar_view.grid_remove()

                # Birth Date
                birth_input.bind("<FocusIn>", lambda event: show_calendar(event, calendar_view, birth_input))
                birth_input.bind("<FocusOut>", lambda event: hide_calendar(event, calendar_view))
                calendar_view.bind("<<DateEntrySelected>>", lambda event: calendar_date_selected(event, calendar_view, birth_input, address_input))

                # Address
                address_label = widget.new_label(body1,"Address")
                address_label.grid(row=3,column=0,padx=10,pady=10,sticky="w")

                address_input = widget.new_input(body1,common.input_bg_color,placeholder_text="Address")
                address_input.configure(font=("Roboto", 16), height=40, width=200)
                address_input.grid(row=3,column=1,padx=10,pady=10)

                # Gender
                gender_label = widget.new_label(body2, "Gender", font=("Roboto", 20))
                gender_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

                gender_combobox = ctk.CTkComboBox(
                    body2,
                    values = ["Male", "Female"],
                    state = "readonly",
                    justify = "center",
                    font = ("Roboto", 16),
                    height = 35,
                    width = 200
                )
                gender_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="w")

                # National_card
                national_card_label = widget.new_label(body2,"ID Card Number")
                national_card_label.grid(row=1,column=0,padx=10,pady=10,sticky="w")

                national_card_input = widget.new_input(body2,common.input_bg_color,placeholder_text="National Card Number")
                national_card_input.configure(font=("Roboto", 16), height=40, width=200)
                national_card_input.grid(row=1,column=1,padx=10,pady=10)

                # Phone
                phone_label = widget.new_label(body2,"Phone Number")
                phone_label.grid(row=2,column=0,padx=10,pady=10,sticky="w")

                phone_input = widget.new_input(body2,common.input_bg_color,placeholder_text="Phone")
                phone_input.configure(font=("Roboto", 16), height=40, width=200)
                phone_input.grid(row=2,column=1,padx=10,pady=10)

                #Frame for footer
                footer = widget.new_frame(edit_student.window,"transparent", 5)
                footer.grid(row=2,column=0,columnspan=2,padx=10,pady=10,sticky="ew")

                footer.grid_columnconfigure(0,weight=1)

                # Inner frame for centering the button
                footer_inner = widget.new_frame(footer, "transparent", 5)
                footer_inner.grid(row=0, column=0, padx=10, pady=10)

                footer_inner.grid_columnconfigure(0, weight=1)

                # get gender from gender_combobox
                def get_gender():
                    if gender_combobox.get() == "Male":
                        return 'M'
                    else:
                        return 'F'

                # Define the admin data
                def get_admin_data():
                    return {
                        'id_card': national_card_input.get(),
                        'last_name': lastname_input.get(),
                        'first_name': firstname_input.get(),
                        'birth' : calendar_view.get(),
                        'gender': get_gender(),
                        'adress': address_input.get(),
                        'phone': phone_input.get(),
                    }

                notification=Notification_frame(footer_inner,"Ceci est test pour un long message dans la barre de notification",1,0,"w")
                # Button confirm
                button_confirm = widget.new_button(
                    footer_inner,
                    "Confirm",
                    
                    lambda : verification(edit_student,get_admin_data(),notification),
                    treeView.row_selected_color,
                    150, 40, 10,
                    hover = signupColor.btn_hover_color,
                    focus = signupColor.btn_focus_color
                )
                button_confirm.grid(row=0,column=0,padx=10,pady=10,sticky="ew")
                button_confirm.configure(font=("Roboto",20))

                # edit_student.always_on_top()
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
        ("Settings", settings_page),
        ("About", about_page),
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
