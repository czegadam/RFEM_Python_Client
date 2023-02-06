import tkinter as tk
from tkinter import ttk

def generate_rfem_model():
    # Placeholder for executing script
    print("Generating RFEM model...")

def load_inputs():
    # Placeholder for loading inputs from database
    print("Loading inputs from database...")

def save_inputs():
    # Placeholder for saving inputs to database
    print("Saving inputs to database...")

root = tk.Tk()
root.title("RFEM Model Generator")
root.configure(bg="#F7F7F7")

frame = ttk.Frame(root, padding=10)
frame.grid(column=0, row=0)

horizontal_spacing_label = ttk.Label(frame, text="Horizontal spacing pattern:")
horizontal_spacing_label.grid(column=0, row=0, pady=10)
horizontal_spacing_entry = ttk.Entry(frame)
horizontal_spacing_entry.grid(column=1, row=0, pady=10)

vertical_spacing_label = ttk.Label(frame, text="Vertical spacing pattern:")
vertical_spacing_label.grid(column=0, row=1, pady=10)
vertical_spacing_entry = ttk.Entry(frame)
vertical_spacing_entry.grid(column=1, row=1, pady=10)

material_label = ttk.Label(frame, text="Material:")
material_label.grid(column=0, row=2, pady=10)
material_entry = ttk.Entry(frame)
material_entry.grid(column=1, row=2, pady=10)

profile_label = ttk.Label(frame, text="Profile:")
profile_label.grid(column=0, row=3, pady=10)
profile_entry = ttk.Entry(frame)
profile_entry.grid(column=1, row=3, pady=10)

fixed_pinned_label = ttk.Label(frame, text="Fixed/Pinned:")
fixed_pinned_label.grid(column=0, row=4, pady=10)
fixed_pinned_var = tk.StringVar(frame)
fixed_pinned_var.set("Fixed")
fixed_pinned_option = ttk.OptionMenu(frame, fixed_pinned_var, "Fixed", "Pinned")
fixed_pinned_option.grid(column=1, row=4, pady=10)

generate_button = ttk.Button(frame, text="Generate RFEM model", command=generate_rfem_model)
generate_button.grid(column=0, row=5, pady=10)

load_button = ttk.Button(frame, text="Load", command=load_inputs)
load_button.grid(column=1, row=5, pady=10)

save_button = ttk.Button(frame, text="Save", command=save_inputs)
save_button.grid(column=2, row=5, pady=10)

root.mainloop()

'''
This script creates a Tkinter UI with 4 input fields for string input, 
a drop-down list for selection between "Fixed" and "Pinned", and buttons 
for generating the RFEM model, loading inputs, and saving inputs. 
The UI has a modern look with pastel colors and is designed with an 
easy-to-use interface. The `generate_rfem_model`, `load_inputs`, and 
`save_inputs` functions are placeholders for now, but you can replace 
them with your own code to perform the relevant actions when the buttons 
are pressed.
'''