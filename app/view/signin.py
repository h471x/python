import tkinter
import customtkinter

from tkcalendar import DateEntry

from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name

path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget

#To use this function we need two argument to store the value of the input in front section :: gender , date

#Back section
def get_selected_date():
    return calendar_view.get_date()

#Radion button
def radiobutton_event(gender_var):
    print(gender_var.get())
#Insertion function
 #Admin
def signup_admin():
    pass

#Front section
def signup_ui ():
    signup = CtkWindow("Register")
    signup.set_size(850,600)

    widget = CtkWidget()
    #To center header frame
    signup.window.grid_columnconfigure(0,weight=1)
    signup.window.grid_columnconfigure(1, weight=1)
    signup.window.grid_rowconfigure(0, weight=1)
    signup.window.grid_rowconfigure(1, weight=1)
    signup.window.grid_rowconfigure(2, weight=1)

    #first frame for the header
    header = widget.new_frame(signup.window, "#1696C4", 5)
    header.grid(row=0,column=0,columnspan=2, padx=10, pady=10,sticky="ew")
    #Center label in header
    header.grid_columnconfigure(0,weight=1)
    signup_label = widget.new_label(header,"Sign Up",font=("Roboto",40))
    # signup_label.pack(expand=True,fill="both", padx=10, pady=10)
    signup_label.grid(row=0,column=0,columnspan=2, padx=10, pady=10,sticky="ew")

    #second frame for body1 that contains the input widgets
    body=widget.new_frame(signup.window,"transparent",5)
    body.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
    #First name
    body1 = widget.new_frame(body, "transparent", 5)
    body2 = widget.new_frame(body, "transparent", 5)

    # body1.pack(expand=True, fill="both", padx=10, pady=10)
    body1.grid(row=1,column=0, padx=10, pady=10,sticky="nsew")
    body2.grid(row=1,column=1, padx=10, pady=10,sticky="nsew")

    firstname_label = widget.new_label(body1,"First name :",font=("Roboto",20))
    firstname_label.grid(row=0,column=0,padx=10,pady=10)

    firstname_input = widget.new_input(body1,"grey",placeholder_text="First name",font=("Roboto",15),corner_radius=10)
    firstname_input.grid(row=0,column=1,padx=10,pady=10)

    #Last name
    lastname_label = widget.new_label(body1,"Last name :",font=("Roboto",20))
    lastname_label.grid(row=1,column=0,padx=10,pady=10,sticky="w")

    lastname_input = widget.new_input(body1,"grey",placeholder_text="Last Name",font=("Roboto",15),corner_radius=10)
    lastname_input.grid(row=1,column=1,padx=10,pady=10)

    #Birth
    birth_label = widget.new_label(body1,"Birth :",font=("Roboto",20))
    birth_label.grid(row=2,column=0,padx=10,pady=10,sticky="w")

    #Calendar
    calendar_view = DateEntry(body1,year=2024,month=6,day=24)
    calendar_view.grid(row=2,column=1,)

    #Gender
    gender_label = widget.new_label(body1,"Gender :",font=("Roboto",20))
    gender_label.grid(row=3,column=0,padx=10,pady=10,sticky="w")
    gender = tkinter.StringVar(value="")

    male_radiobutton = customtkinter.CTkRadioButton(body1, text="Male",command=lambda: radiobutton_event(gender),variable=gender,value='M')
    female_radiobutton = customtkinter.CTkRadioButton(body1, text="Female",command=lambda: radiobutton_event(gender),variable=gender,value='F')
    male_radiobutton.grid(row=3,column=1,sticky="w")
    female_radiobutton.grid(row=3,column=2,sticky="w")

    #Address
    address_label = widget.new_label(body1,"Address :")
    address_label.grid(row=4,column=0,padx=10,pady=10,sticky="w")

    address_input = widget.new_input(body1,"grey",placeholder_text="Address")
    address_input.grid(row=4,column=1,padx=10,pady=10)

    #National_card
    national_card_label=widget.new_label(body2,"National card number :")
    national_card_label.grid(row=0,column=0,padx=10,pady=10,sticky="w")

    national_card_input = widget.new_input(body2,"grey",placeholder_text="National card")
    national_card_input.grid(row=0,column=1,padx=10,pady=10)

    #Phone
    phone_label = widget.new_label(body2,"Phone number :")
    phone_label.grid(row=1,column=0,padx=10,pady=10,sticky="w")

    phone_input = widget.new_input(body2,"grey",placeholder_text="Phone")
    phone_input.grid(row=1,column=1,padx=10,pady=10)

    #Username
    username_label = widget.new_label(body2,"Username :")
    username_label.grid(row=2,column=0,padx=10,pady=10,sticky="w")

    username_input = widget.new_input(body2,"grey",placeholder_text="Username")
    username_input.grid(row=2,column=1,padx=10,pady=10)

    #Password
    password_label = widget.new_label(body2,"Password:")
    password_label.grid(row=3,column=0,padx=10,pady=10,sticky="w")

    password_input = widget.new_input(body2,"grey",placeholder_text="Password")
    password_input.grid(row=3,column=1,padx=10,pady=10)

    confirm_label = widget.new_label(body2,"Confirm:")
    confirm_label.grid(row=4,column=0,padx=10,pady=10,sticky="w")

    confirm_input = widget.new_input(body2,"grey",placeholder_text="Password")
    confirm_input.grid(row=4,column=1,padx=10,pady=10)
    #Frame for footer
    footer=widget.new_frame(signup.window,"transparent", 5)
    footer.grid(row=2,column=0,columnspan=2,padx=10,pady=10,sticky="ew")
    footer.grid_columnconfigure(0,weight=1)
    # Inner frame for centering the button
    footer_inner = widget.new_frame(footer, "transparent", 5)
    footer_inner.grid(row=0, column=0, padx=10, pady=10)
    footer_inner.grid_columnconfigure(0, weight=1)
    #Button signup
    button_signup=widget.new_button(footer_inner,"Sign Up",signup_admin(),"#1696C4",hover="#7DD61E",focus="#7DD61E")
    button_signup.grid(row=0,column=0,padx=10,pady=10,sticky="ew")
    button_signup.configure(font=("Roboto",20))

    signup.open_centered()

if __name__ == '__main__':
    signup_ui()
