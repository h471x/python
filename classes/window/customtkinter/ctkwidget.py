import customtkinter

# ctk_widget base class
class CtkWidget:
    def __init__(self):
        self.ctk = customtkinter

    def clear_widget(self, widget):
        for child in widget.winfo_children():
            child.destroy()

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

    def new_label(self, parent, text, image=None):
        label = self.ctk.CTkLabel(master=parent, text=f"{text}", image=image)
        label.bind("<Enter>", lambda event: None)
        label.bind("<Leave>", lambda event: None)
        return label

    def new_input(self, parent, color):
        return self.ctk.CTkEntry(
            master=parent,
            fg_color=f"{color}",
            border_width=0
        )

# extended class CtkFrame
class CustomCtkFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_color = self.cget("fg_color")
        self.focus_color = None
        self.is_focused = False

    def set_focus_color(self, color):
        self.focus_color = color

    def on_hover(self, hover_color):
        def hovered(event):
            self.configure(fg_color=hover_color)

        def blurred(event):
            if self.is_focused:
                if self.focus_color:
                    self.configure(fg_color=self.focus_color)
                else:
                    self.configure(fg_color=self.original_color)
            else:
                self.configure(fg_color=self.original_color)

        self.bind("<Enter>", hovered)
        self.bind("<Leave>", blurred)

    def on_click(self, function):
        def click_event(event):
            if self.focus_color:
                self.set_focus()
            function()
        self.bind("<Button-1>", click_event)

    def set_focus(self):
        self.is_focused = True
        if self.focus_color:
            self.configure(fg_color=self.focus_color)

    def clear_focus(self):
        self.is_focused = False
        if self.focus_color:
            self.configure(fg_color=self.original_color)
