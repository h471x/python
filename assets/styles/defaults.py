from tkinter import ttk

def configure_styles():
    style = ttk.Style()

    # Configure Treeview headers
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"), padding=[10, 10, 10, 10])

    # Configure Treeview rows
    style.configure("Treeview", font=("Arial", 12), rowheight=40)  # Adjust row height as needed
