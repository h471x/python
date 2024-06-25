import tkinter
from tkinter import ttk
import customtkinter

from tkcalendar import DateEntry
from datetime import datetime

from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name

path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget

from app.view.dashboard import dashboard_ui

from assets.styles.colors import *
from app.controllers.admin import *

# To use this function we need two argument to store the value of the input in front section :: gender , date

# Back section
def get_selected_date():
    return calendar_view.get_date()

# Radion button
def radiobutton_event(gender_var):
    gender_var.get()

def close_window(window):
    return lambda: (
        window.close()
    )

# Insertion function
# Admin
def signup_admin(admin_data):
    admin_insert(admin_data)
    # dashboard_ui()
    # close_window(window)

# Function to handle date selection
def select_date(entry, date_entry, next_entry):
    selected_date = date_entry.get_date()
    entry.delete(0, tkinter.END)
    entry.insert(0, selected_date)
    next_entry.focus_set()

# Front section
def signup_ui ():
    signup = CtkWindow("Register")
    signup.set_size(850,600)
    widget = CtkWidget()

    # To center header frame
    signup.window.grid_columnconfigure(0,weight=1)
    signup.window.grid_columnconfigure(1, weight=1)
    signup.window.grid_rowconfigure(0, weight=1)
    signup.window.grid_rowconfigure(1, weight=1)
    signup.window.grid_rowconfigure(2, weight=1)

    # first frame for the header
    header = widget.new_frame(signup.window, signup_header_color, 5)
    header.grid(row=0,column=0,columnspan=2, padx=10, pady=10,sticky="ew")

    # Center label in header
    header.grid_columnconfigure(0,weight=1)
    signup_label = widget.new_label(header,"Sign Up",font=("Roboto",40))

    # signup_label.pack(expand=True,fill="both", padx=10, pady=10)
    signup_label.grid(row=0,column=0,columnspan=2, padx=10, pady=10,sticky="ew")

    # second frame for body1 that contains the input widgets
    body=widget.new_frame(signup.window,"transparent",5)
    body.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    # First name
    body1 = widget.new_frame(body, "transparent", 5)
    body2 = widget.new_frame(body, "transparent", 5)

    # body1.pack(expand=True, fill="both", padx=10, pady=10)
    body1.grid(row=1,column=0, padx=10, pady=10,sticky="nsew")
    body2.grid(row=1,column=1, padx=10, pady=10,sticky="nsew")

    firstname_label = widget.new_label(body1,"First name :",font=("Roboto",20))
    firstname_label.grid(row=0,column=0,padx=10,pady=10)

    firstname_input = widget.new_input(body1,input_bg_color,placeholder_text="First name",font=("Roboto",15),corner_radius=10)
    firstname_input.grid(row=0,column=1,padx=10,pady=10)

    # focus first_name input on startup
    firstname_input.focus_set()

    # Last name
    lastname_label = widget.new_label(body1,"Last name :",font=("Roboto",20))
    lastname_label.grid(row=1,column=0,padx=10,pady=10,sticky="w")

    lastname_input = widget.new_input(body1,input_bg_color,placeholder_text="Last Name",font=("Roboto",15),corner_radius=10)
    lastname_input.grid(row=1,column=1,padx=10,pady=10)

    # Birth
    birth_label = widget.new_label(body1,"Birth :",font=("Roboto",20))
    birth_label.grid(row=2,column=0,padx=10,pady=10,sticky="w")

    # Calculate the date 18 years ago
    today = datetime.today()
    initial_birth_date = today.replace(year=today.year - 18)

    # Calculate the last date of the previous year
    max_date = datetime(today.year - 1, 12, 31)

    # Birth input
    birth_input = widget.new_input(
        body1,
        input_bg_color,
        placeholder_text="Date Of Birth",
        font=("Roboto",15),
        corner_radius=10,
    )
    birth_input.grid(row=2,column=1,padx=10,pady=10)

    # Create DateEntry with the calculated initial date and max date
    calendar_view = DateEntry(
        birth_input,
        year=initial_birth_date.year,
        month=initial_birth_date.month,
        day=initial_birth_date.day,
        state="readonly",
        style='my.DateEntry',
        background='darkblue',
        foreground='white',
        borderwidth=2,
        maxdate=max_date
    )
    calendar_view.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    # Adjust size of the calendar popup
    def configure_calendar_popup():
        popup = calendar_view._calendar.winfo_toplevel()
        popup.geometry("300x200")
        popup.configure(background="darkblue")

    # Initially hide the calendar part
    calendar_view._calendar.winfo_toplevel().withdraw()
    calendar_view.grid_remove()

    # Bind calendar date selection to update the birth_input field
    def show_calendar(event):
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

    def hide_calendar(event):
        calendar_view._calendar.winfo_toplevel().withdraw()

    def calendar_date_selected(event):
        select_date(birth_input, calendar_view, address_input)

    birth_input.bind("<FocusIn>", show_calendar)
    birth_input.bind("<FocusOut>", hide_calendar)
    calendar_view.bind("<<DateEntrySelected>>", calendar_date_selected)

    # Address
    address_label = widget.new_label(body1,"Address :")
    address_label.grid(row=3,column=0,padx=10,pady=10,sticky="w")

    address_input = widget.new_input(body1,input_bg_color,placeholder_text="Address")
    address_input.grid(row=3,column=1,padx=10,pady=10)

    # Gender
    gender_label = widget.new_label(body1,"Gender :",font=("Roboto",20))
    gender_label.grid(row=4,column=0,padx=10,pady=10,sticky="w")
    gender = tkinter.StringVar(value="")

    male_radiobutton = customtkinter.CTkRadioButton(
        body1, text="Male",
        command=lambda: radiobutton_event(gender),
        variable=gender, value='M'
    )

    female_radiobutton = customtkinter.CTkRadioButton(
        body1, text="Female",
        command=lambda: radiobutton_event(gender),
        variable=gender, value='F'
    )

    male_radiobutton.grid(row=4,column=1,sticky="w")
    female_radiobutton.grid(row=4,column=2,sticky="w")

    # Adjusted grid and padx for male and female radio buttons
    male_radiobutton.grid(row=4, column=1, sticky="w", padx=5)
    female_radiobutton.grid(row=4, column=2, sticky="w", padx=5)

    # National_card
    national_card_label = widget.new_label(body2,"National card number :")
    national_card_label.grid(row=0,column=0,padx=10,pady=10,sticky="w")

    national_card_input = widget.new_input(body2,input_bg_color,placeholder_text="National card")
    national_card_input.grid(row=0,column=1,padx=10,pady=10)

    # Phone
    phone_label = widget.new_label(body2,"Phone number :")
    phone_label.grid(row=1,column=0,padx=10,pady=10,sticky="w")

    phone_input = widget.new_input(body2,input_bg_color,placeholder_text="Phone")
    phone_input.grid(row=1,column=1,padx=10,pady=10)

    #Username
    username_label = widget.new_label(body2,"Username :")
    username_label.grid(row=2,column=0,padx=10,pady=10,sticky="w")

    username_input = widget.new_input(body2,input_bg_color,placeholder_text="Username")
    username_input.grid(row=2,column=1,padx=10,pady=10)

    #Password
    password_label = widget.new_label(body2,"Password:")
    password_label.grid(row=3,column=0,padx=10,pady=10,sticky="w")

    password_input = widget.new_input(body2,input_bg_color,placeholder_text="Password")
    password_input.grid(row=3,column=1,padx=10,pady=10)

    confirm_label = widget.new_label(body2,"Confirm:")
    confirm_label.grid(row=4,column=0,padx=10,pady=10,sticky="w")

    confirm_input = widget.new_input(body2,input_bg_color,placeholder_text="Password")
    confirm_input.grid(row=4,column=1,padx=10,pady=10)

    #Frame for footer
    footer = widget.new_frame(signup.window,"transparent", 5)
    footer.grid(row=2,column=0,columnspan=2,padx=10,pady=10,sticky="ew")
    footer.grid_columnconfigure(0,weight=1)

    # Inner frame for centering the button
    footer_inner = widget.new_frame(footer, "transparent", 5)
    footer_inner.grid(row=0, column=0, padx=10, pady=10)
    footer_inner.grid_columnconfigure(0, weight=1)

    # Define the admin data
    def get_admin_data():
        return {
            'id_card': national_card_input.get(),
            'last_name': lastname_input.get(),
            'first_name': firstname_input.get(),
            'birth' : calendar_view.get(),
            'gender': gender.get(),
            'adress': address_input.get(),
            'phone': phone_input.get(),
            'username': username_input.get(),
            'password': password_input.get(),
        }

    # Button signup
    button_signup = widget.new_button(
        footer_inner,
        "Sign Up",
        lambda: signup_admin(get_admin_data()),
        signup_btn_color,
        hover=signup_btn_hover_color,
        focus=signup_btn_focus_color
    )
    button_signup.grid(row=0,column=0,padx=10,pady=10,sticky="ew")
    button_signup.configure(font=("Roboto",20))

    signup.open_centered()

if __name__ == '__main__':
    signup_ui()
