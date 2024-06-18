from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name

path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget

def signin_ui ():
    signin = CtkWindow("Register")
    signin.set_size(800,600)

    widget = CtkWidget()
    frame = widget.new_frame(signin.window, "transparent", 5)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    signin.open_centered()

if __name__ == '__main__':
    signin_ui()
