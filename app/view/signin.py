from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name

path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget

def signup_ui ():
    signup = CtkWindow("Register")
    signup.set_size(800,600)

    widget = CtkWidget()
    header = widget.new_frame(signup.window, "transparent", 5)
    header.pack(expand=True, fill="both", padx=10, pady=10)
    signup_label=widget.new_label(header,"Sign Up",font=("Roboto",40))
    signup_label.pack(expand=True,fill="both", padx=10, pady=10)
    

    signup.open_centered()

if __name__ == '__main__':
    signup_ui()
