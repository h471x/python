import customtkinter
from platform import system as getSystem

class CtkWindow:
    def __init__(self, title):
        self.ctk = customtkinter
        self.window = self.ctk.CTk()
        self.ctk.set_appearance_mode("System")
        self.ctk.set_default_color_theme("blue")
        self.minWidth = 800
        self.minHeight = 500
        self.window.title(f"{title}")
        self.setSize(self.minWidth, self.minHeight)

    def maximise(self):
        maximiseWindow = {
            'Windows': "state('zoomed')",
            'Linux': "attributes('-zoomed', True)",
            'Darwin': "attributes('-fullscreen', True)"
        }.get(getSystem(),lambda: print("Unsupported operating system"))

        eval(f"self.window.{maximiseWindow}")

    def setSize(self, width, height):
        self.window.geometry(f"{width}x{height}")

    def makeResizable(self):
        self.window.resizable(width=True, height=True)

    def open(self):
        self.window.mainloop()

    def openMaximised(self):
        self.window.after(0, lambda:self.maximise())
        self.open()

    def newButton(self, parent, content, action):
        return self.ctk.CTkButton(
            master=parent,
            text=f"{content}",
            command=action
        )
