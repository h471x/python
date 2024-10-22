import tkinter as tk
import customtkinter
from platform import system as get_system

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

    def maximise(self):
        maximise_window = {
            'Windows': "state('zoomed')",
            'Linux': "attributes('-zoomed', True)",
            'Darwin': "attributes('-fullscreen', True)"
        }.get(get_system(), lambda: print("Unsupported operating system"))

        eval(f"self.window.{maximise_window}")

    def set_size(self, width, height):
        self.min_width = width
        self.min_height = height
        self.window.minsize(self.min_width, self.min_height)
        self.window.geometry(f"{self.min_width}x{self.min_height}")

    def make_resizable(self):
        self.window.resizable(width=True, height=True)

    def not_resizable(self):
        self.window.resizable(width=False, height=False)

    def open(self):
        self.window.mainloop()

    def open_maximised(self):
        self.window.after(0, lambda: self.maximise())
        self.open()

    def open_centered(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width // 2) - (self.min_width // 2)
        y = (screen_height // 2) - (self.min_height // 2)

        self.window.geometry(f"{self.min_width}x{self.min_height}+{x}+{y}")
        self.open()

    def always_on_top(self):
        self.window.attributes("-topmost", True)
        self.focus_window()

    def focus_window(self):
        if self.window.winfo_exists():
            self.window.focus_force()
            self.window.after(100, self.focus_window)

    def close(self):
        self.window.destroy()
