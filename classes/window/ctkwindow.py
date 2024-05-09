import customtkinter as ctk

class CtkWindow:
    def __init__(self):
        self.window = ctk.CTk()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

    def maximise(self):
        self.window.state('zoomed')

    def openMaximised(self):
        self.window.after(0, lambda:self.maximise())
        self.window.mainloop()
