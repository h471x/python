from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name

path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget

#Front
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
    firstname_label=widget.new_label(body,"First Name :",font=("Roboto",20))
    firstname_label.pack(padx=10,pady=10)
    firstname_input=widget.new_input(body,"grey")
    firstname_input.pack(padx=10,pady=10)

    lastname_label=widget.new_label(body,"Last Name :",font=("Roboto",20))
    lastname_label.pack(padx=10,pady=10)
    lastname_input=widget.new_input(body,"grey")
    lastname_input.pack(padx=10,pady=10)

    birth_label=widget.new_label(body,"Birth :",font=("Roboto",20))
    birth_label.pack(padx=10,pady=10)
    

    signup.open_centered()

if __name__ == '__main__':
    signup_ui()
