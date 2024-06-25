import tkinter as tk
from tkinter import ttk

import os
from PIL import ImageFont

from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name

path.append(abs_path(join_path(dir_name(__file__), '..', '..')))

from assets.styles.colors import *

def load_font(window):
    font_path = os.path.abspath("assets/fonts/NerdFont.ttf")
    font_family = "NerdFont"

    try:
        if font_family not in window.tk.call('font', 'names'):
            window.tk.call(
                'font', 'create', font_family,
                '-family', font_family,
            )
    except tk.TclError as e:
        print(f"Error loading font: {e}")
        font_family = "TkDefaultFont"

    return font_family

def configure_table_styles(window):
    style = ttk.Style()
    font_family = load_font(window)

    # Configure Treeview headers
    style.configure(
        "Treeview.Heading",
        font=(font_family, 15, "bold"),
        padding=[20, 20, 20, 20],
        background=header_color,
        foreground=text_color,
    )

    style.map(
        "Treeview.Heading",
        background=[("hover", header_color)]
    )

    # Configure Treeview rows
    style.configure(
        "Treeview",
        font=(font_family, 18),
        rowheight=70,
        background="#262626",
        foreground=text_color,
        fieldbackground="#262626"
    )

    # Configure the style for selected row
    style.map("Treeview",
        background=[("selected", row_selected_color)],
        foreground=[("selected", text_color)]
    )
