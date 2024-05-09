import customtkinter

class CtkWindow:
    def __init__(self, title):
        self.ctk = customtkinter
        self.window = self.ctk.CTk()
        self.ctk.set_appearance_mode("System")
        self.ctk.set_default_color_theme("blue")
        self.window.title(f"{title}")

    def maximise(self):
        self.window.state('zoomed')

    def setSize(self, width, height):
        self.window.geometry(f"{width}x{height}")

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
