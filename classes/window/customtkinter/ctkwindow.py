import tkinter as tk
import customtkinter
from platform import system as get_system
# from pathlib import Path
# ASSETS_PATH = Path(__file__).resolve().parent.parent.parent / "assets"

class CtkWindow:
    def __init__(self, title=None):
        self.ctk = customtkinter
        self.window = self.ctk.CTk()
        self.ctk.set_appearance_mode("System")
        self.ctk.set_default_color_theme("blue")
        self.min_width = 800
        self.min_height = 500
        self.window.update()
        self.window.minsize(self.min_width, self.min_height)
        self.window.title(title) if title else None
        self.set_size(self.min_width, self.min_height)
        # self.logo = self.ctk.PhotoImage(file=ASSETS_PATH / "python.ico")
        # self.window.call('wm', 'iconphoto', self.window._w, self.logo)

    def maximise(self):
        maximise_window = {
            'Windows': "state('zoomed')",
            'Linux': "attributes('-zoomed', True)",
            'Darwin': "attributes('-fullscreen', True)"
        }.get(get_system(), lambda: print("Unsupported operating system"))

        eval(f"self.window.{maximise_window}")

    def set_size(self, width, height):
        self.window.minsize(width, height)
        self.window.geometry(f"{width}x{height}")


    def make_resizable(self):
        self.window.resizable(width=True, height=True)

    def open(self):
        self.window.mainloop()

    def open_maximised(self):
        self.window.after(0, lambda: self.maximise())
        self.open()

    def open_centered(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        self.window.minsize(self.min_width, self.min_height)

        x = (screen_width // 2) - (self.min_width // 2)
        y = (screen_height // 2) - (self.min_height // 2)

        self.window.geometry(f"{self.min_width}x{self.min_height}+{x}+{y}")
        self.open()

    def close(self):
        self.window.destroy()
