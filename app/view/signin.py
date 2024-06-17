from dashboard import close_window
import customtkinter as ctk
from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name

path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from classes.window.customtkinter.ctkwindow import CtkWindow
from classes.window.customtkinter.ctkwidget import CtkWidget


def signin_ui ():
    signin = CtkWindow("Register")
    signin.set_size(800,600)
    signin.open()
    

