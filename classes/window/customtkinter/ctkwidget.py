import customtkinter

# CtkWidget Base Class
class CtkWidget:
    def __init__(self):
        self.ctk = customtkinter

    def newButton(self, parent, text, btnCommand):
        return self.ctk.CTkButton(
            master=parent,
            text=f"{text}",
            command=btnCommand
        )

    def newFrame(self, parent, color, corner_radius, width=None, height=None):
        properties = {
            "master": parent,
            "fg_color": color,
            "corner_radius": corner_radius
        }
        if width is not None:
            properties["width"] = width
        if height is not None:
            properties["height"] = height
        return CustomCTkFrame(**properties)

# Extended class CTkFrame
class CustomCTkFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.originalColor = self.cget("fg_color")

    def onHover(self, hoverColor):
        def onHover(event):
            self.configure(fg_color=hoverColor)

        def onBlur(event):
            self.configure(fg_color=self.originalColor)

        self.bind("<Enter>", onHover)
        self.bind("<Leave>", onBlur)
