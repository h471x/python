import customtkinter
from PIL import Image

# ctk_widget base class
class CtkWidget:
    def __init__(self):
        self.ctk = customtkinter

    def clear_widget(self, widget):
        for child in widget.winfo_children():
            child.destroy()

    def new_button(
        self, parent, text, btn_command,
        color=None, width=None, height=None,
        radius=None, hover=None, focus=None
    ):
        button_params = {
            "master": parent,
            "text": f"{text}",
            "command": btn_command,
        }
        if color:
            button_params["fg_color"] = f"{color}"
        if width:
            button_params["width"] = width
        if height:
            button_params["height"] = height
        if radius:
            button_params["corner_radius"] = radius
        if hover:
            button_params["hover_color"] = hover

        button = CustomCtkButton(**button_params)
        if focus:
            button.set_focus_color(f"{focus}")
        return button

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

    def new_label(self, parent, text, image=None ,font=("Roboto",20)):
        label = self.ctk.CTkLabel(master=parent, text=f"{text}", image=image,font=font)
        label.bind("<Enter>", lambda event: None)
        label.bind("<Leave>", lambda event: None)
        return label

    def new_input(self, parent, color,text_color="white",font=("Roboto",15),corner_radius=10,placeholder_text=None,placeholder_text_color="white"):
        return self.ctk.CTkEntry(
            master=parent,
            fg_color=f"{color}",
            border_width=0,
            text_color=text_color,
            font=font,
            corner_radius=corner_radius,
            placeholder_text=placeholder_text,
            placeholder_text_color=placeholder_text_color
        )

    def new_image(self, parent, image_path, width=None, height=None):
        img_data = Image.open(image_path)
        img = self.ctk.CTkImage(light_image=img_data, dark_image=img_data)
        frame = self.ctk.CTkFrame(master=parent, width=width, height=height)
        label = self.ctk.CTkLabel(master=frame, image=img, text="")
        label.pack(expand=True, fill='both')
        frame.pack_propagate(False)
        return frame

    def new_dropdown(self, parent, values, width, height):
        return self.ctk.CTkComboBox(
            master=parent,
            values=values,
            width=width,
            height=height
        )

# extended class CustomCtkButton
class CustomCtkButton(customtkinter.CTkButton):
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

    def set_focus(self):
        self.is_focused = True
        if self.focus_color:
            self.configure(fg_color=self.focus_color)

    def clear_focus(self):
        self.is_focused = False
        if self.focus_color:
            self.configure(fg_color=self.original_color)

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
