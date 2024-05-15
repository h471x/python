import customtkinter

class CtkWidget:
    def __init__(self):
        self.ctk = customtkinter

    def newButton(self, parent, text, btnCommand):
        return self.ctk.CTkButton(
            master=parent,
            text=f"{text}",
            command=btnCommand
        )
