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
#Calendar
def get_selected_date():
    return calendar_view.get_date()
#Radion button
def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

#Front section
def signup_ui ():
    signup = CtkWindow("Register")
    signup.set_size(800,600)
    widget = CtkWidget()

    #first frame for the header
    header = widget.new_frame(signup.window, "transparent", 5,800,100)
    header.pack(expand=True, fill="both", padx=10, pady=10)
    signup_label=widget.new_label(header,"Sign Up",font=("Roboto",40))
    signup_label.pack(expand=True,fill="both", padx=10, pady=10)

    #second frame for body that contains the input widgets
    body = widget.new_frame(signup.window, "transparent", 5)
    body.pack(expand=True, fill="both", padx=10, pady=10)
    firstname_label=widget.new_label(body,"First name :",font=("Roboto",20))
    firstname_label.pack(padx=10,pady=10)
    firstname_input=widget.new_input(body,"grey",placeholder_text="First name",font=("Roboto",15),corner_radius=10)
    firstname_input.pack(padx=10,pady=10)

    lastname_label=widget.new_label(body,"Last name :",font=("Roboto",20))
    lastname_label.pack(padx=10,pady=10)
    lastname_input=widget.new_input(body,"grey",placeholder_text="Last Name",font=("Roboto",15),corner_radius=10)
    lastname_input.pack(padx=10,pady=10)

    birth_label=widget.new_label(body,"Birth :",font=("Roboto",20))
    birth_label.pack(padx=10,pady=10)
    #Calendar
    calendar_view=DateEntry(body,year=2024,month=6,day=24)
    calendar_view.pack()

    gender_label=widget.new_label(body,"Gender :",font=("Roboto",20))
    gender_label.pack(padx=10,pady=10)
    gender=tkinter.StringVar(value="")
    male_radiobutton=customtkinter.CTkRadioButton(body, text="Male",command=radiobutton_event,variable=gender,value='m')
    female_radiobutton=customtkinter.CTkRadioButton(body, text="Female",command=radiobutton_event,variable=gender,value='f')
    male_radiobutton.pack()
    female_radiobutton.pack()
    

    signup.open_centered()

if __name__ == '__main__':
    G="Nothing"
    signup_ui()
