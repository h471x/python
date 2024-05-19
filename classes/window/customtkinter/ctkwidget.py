import customtkinter

# ctk_widget base class
class CtkWidget:
    def __init__(self):
        self.ctk = customtkinter

    def new_button(self, parent, text, btn_command):
        return self.ctk.CTkButton(
            master=parent,
            text=f"{text}",
            command=btn_command
        )

    def new_frame(self, parent, color, corner_radius, width=None, height=None):
        properties = {
            "master": parent,
            "fg_color": color,
            "corner_radius": corner_radius
        }
        if width is not None:
            properties["width"] = width
        if height is not None:
            properties["height"] = height
        return CustomCtkFrame(**properties)

# extended class CtkFrame
class CustomCtkFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_color = self.cget("fg_color")

    def on_hover(self, hover_color):
        def on_hover(event):
            self.configure(fg_color=hover_color)

        def on_blur(event):
            self.configure(fg_color=self.original_color)

        self.bind("<Enter>", on_hover)
        self.bind("<Leave>", on_blur)

    def on_click(self, function):
        self.bind("<Button-1>", lambda event: function())
