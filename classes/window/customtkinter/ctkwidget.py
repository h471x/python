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

    def newFrame(self, parent, color, radius, width=None, height=None):
        properties = {
            "master": parent,
            "corner_radius": radius,
            "fg_color": color
        }
        if width:
            properties["width"] = width
        if height:
            properties["height"] = height
        return self.ctk.CTkFrame(**properties)

