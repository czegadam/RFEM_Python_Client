import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("RFEM Model Generator")

# Define the styles for the UI elements
style = ttk.Style()
style.configure("TFrame", background="darkblue")
style.configure("TLabel", background="darkblue", foreground="white", font=("TkDefaultFont", 16))
style.configure("TEntry", font=("TkDefaultFont", 16))
style.configure("TButton", font=("TkDefaultFont", 16), background="darkgrey", foreground="white")

# Create the main frame
main_frame = ttk.Frame(root, style="TFrame")
main_frame.grid(column=0, row=0, padx=30, pady=30)

# Create the input fields
ttk.Label(main_frame, text="Horizontal spacing pattern", style="TLabel").grid(column=0, row=0, sticky="W")
horizontal_spacing = ttk.Entry(main_frame)
horizontal_spacing.grid(column=1, row=0)

ttk.Label(main_frame, text="Vertical spacing pattern", style="TLabel").grid(column=0, row=1, sticky="W")
vertical_spacing = ttk.Entry(main_frame)
vertical_spacing.grid(column=1, row=1)

ttk.Label(main_frame, text="Material", style="TLabel").grid(column=0, row=2, sticky="W")
material = ttk.Entry(main_frame)
material.grid(column=1, row=2)

ttk.Label(main_frame, text="Profile", style="TLabel").grid(column=0, row=3, sticky="W")
profile = ttk.Entry(main_frame)
profile.grid(column=1, row=3)

# Create the list of selection input
ttk.Label(main_frame, text="Fixed/Pinned", style="TLabel").grid(column=0, row=4, sticky="W")
fixed_pinned = tk.StringVar()
fixed_pinned.set("Fixed")
fixed_pinned_select = ttk.OptionMenu(main_frame, fixed_pinned, "Fixed", "Pinned")
fixed_pinned_select.grid(column=1, row=4)

# Create the "Generate RFEM model" button
def generate_rfem_model():
    # Placeholder for executing the script
    print("Generating RFEM model...")

generate_button = ttk.Button(main_frame, text="Generate RFEM model", style="TButton", command=generate_rfem_model)
generate_button.grid(column=0, row=5, columnspan=2, pady=20)

# Create the "Load" button
def load_inputs():
    # Placeholder for loading inputs from database
    print("Loading inputs...")

load_button = ttk.Button(main_frame, text="Load", style="TButton", command=load_inputs)
load_button.grid(column=0, row=6, pady=10)

# Create the "Save" button
def save_inputs():
    # Placeholder for saving inputs to database
    print("Saving inputs...")

save_button = ttk.Button(main_frame, text="Save", style="TButton", command=save_inputs)
save_button.grid(column=1, row=6, pady=10)

# Run the main loop
root.mainloop()
