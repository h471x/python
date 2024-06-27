import customtkinter
from PIL import Image
from sys import path
from os.path import abspath as abs_path, join as join_path, dirname as dir_name

path.append(abs_path(join_path(dir_name(__file__), '..', '..')))
from assets.styles.colors import *

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
        radius=None, hover=None, focus=None, font=("Roboto",15)
    ):
        button_params = {
            "master": parent,
            "text": f"{text}",
            "command": btn_command,
            "font" : font
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

    def new_label(
        self, parent, text, image=None,
        font=("Roboto",20)
    ):
        label = self.ctk.CTkLabel(master=parent, text=f"{text}", image=image,font=font)
        label.bind("<Enter>", lambda event: None)
        label.bind("<Leave>", lambda event: None)
        return label

    def new_input(
        self, parent, color,
        text_color="white", font=("Roboto",15),
        corner_radius=10, placeholder_text=None,
        placeholder_text_color="grey"
    ):
        return self.ctk.CTkEntry(
            master = parent,
            fg_color = f"{color}",
            border_width = 0,
            text_color = text_color,
            font = font,
            corner_radius = corner_radius,
            placeholder_text = placeholder_text,
            placeholder_text_color = placeholder_text_color
        )

    def new_image(self, parent, image_path, width=None, height=None):
        img_data = Image.open(image_path)
        img = self.ctk.CTkImage(light_image=img_data, dark_image=img_data)
        frame = self.ctk.CTkFrame(master=parent, width=width, height=height)
        label = self.ctk.CTkLabel(master=frame, image=img, text="")
        label.pack(expand=True, fill='both')
        frame.pack_propagate(False)
        return frame

    def new_dropdown(
        self, parent, values,
        width, height,
        justify = None
    ):
        return self.ctk.CTkComboBox(
            master = parent,
            values = values,
            width = width,
            height = height,
            justify = f"{justify}" if justify else None,
        )

    def new_radio(self, parent, text, command, variable, value):
        return self.ctk.CTkRadioButton(
            parent,
            text = f"{text}",
            command = command,
            variable = variable,
            value = value
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

class Notification_frame(customtkinter.CTkFrame):
    def __init__(self, parent,message,posrow,poscolumn,stickyval, delay=3000, color=row_selected_color, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #Attribut 
        # self.frame=frame
        self.frow=posrow
        self.fcol=poscolumn
        self.stick=f"{stickyval}"
        # Configuration des couleurs
        self.configure(fg_color=color)  # Utilisation d'une couleur de fond
        
        # Ajouter un label au cadre de notification
        notif_label = customtkinter.CTkLabel(self, text=message, text_color="white", font=("Arial", 14))
        notif_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        
        # Ajouter un bouton pour fermer la notification
        close_button = customtkinter.CTkButton(self, text="Fermer", text_color=color, fg_color="white", command=self.destroy)
        close_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        
        # Ajouter le cadre de notification à la fenêtre principale en bas
        
        # Fermer automatiquement la notification après 'delay' millisecondes


    # if self.frame.winfo_ismapped():
    #     self.frame.grid_forget()
        # Ajouter le cadre de notification à la fenêtre principale a la place de l'ancien frame
    def notif_show_success(self,delay=3000):
        self.configure(fg_color="grey")
        self.grid(row=self.frow, column=self.fcol, padx=10, pady=10, sticky=self.stick)
        self.after(delay, self.grid_remove)
