from tkinter import ttk

def configure_table_styles():
    style = ttk.Style()

    # Configure Treeview headers
    style.configure(
        "Treeview.Heading",
        font=("Arial", 12, "bold"),
        padding=[20, 20, 20, 20],
        background="#000000",
        foreground="#FFFFFF",
    )

    # Configure Treeview rows
    style.configure(
        "Treeview",
        font=("Arial", 12),
        rowheight=60,
        background="#202020",
        foreground="#FFFFFF",
        fieldbackground="#202020"
    )

    # Configure the style for selected row
    # style.map("Treeview",
    #           background=[("selected", "#347083")],  # Background color when selected
    #           foreground=[("selected", "#FFFFFF")])  # Foreground color when selected
