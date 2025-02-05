import tkinter as tk
from gui.second_window import create_second_window

def submit():
    """Handles the submit action when the user clicks the Submit button."""
    # Get the selected checkbox items
    selected_items = []
    for var, item in zip(checkbox_vars, checkbox_items):
        if var.get() == 1:
            selected_items.append(item)
    
    # Show the second window and update the output text field
    create_second_window(selected_items)

def add_checkboxes(root: tk.Tk, label: str, items: list):
    """Adds checkboxes for the given items to the window."""
    checkbox_label = tk.Label(root, text=label, font=('Arial', 12))
    checkbox_label.pack(pady=5)
    
    global checkbox_vars
    checkbox_vars = []
    
    # Create checkboxes for each item in the list
    for item in items:
        var = tk.IntVar(value=1)  # Set default to checked
        checkbox_vars.append(var)
        checkbox = tk.Checkbutton(root, text=item, variable=var, font=('Arial', 10))
        checkbox.pack(anchor='w')

def create_first_window(title, items):
    """Creates the main window with checkboxes and the Submit button."""
    root = tk.Tk()
    root.title(title)
    root.geometry("500x400")
    
    # Title label
    title_label = tk.Label(root, text="PPE Detection", font=('Arial', 16))
    title_label.pack(pady=20)

    # # Define the items for checkboxes
    global checkbox_items
    checkbox_items = items
    
    # Add checkboxes to the window
    add_checkboxes(root, "Select features:", checkbox_items)
    
    # Submit button
    submit_button = tk.Button(root, text="Submit", command=lambda: submit(), font=('Arial', 12))
    submit_button.pack(pady=10)
    
    # Start the Tkinter event loop
    root.mainloop()
