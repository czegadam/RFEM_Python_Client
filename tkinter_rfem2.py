import tkinter as tk
from tkinter import ttk

def generate_model():
    print("Generating RFEM model...")

def save_inputs():
    print("Saving inputs...")

def load_inputs():
    print("Loading inputs...")

root = tk.Tk()
root.title("RFEM Model Generator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

horizontal_spacing = tk.StringVar()
vertical_spacing = tk.StringVar()
material = tk.StringVar()
profile = tk.StringVar()
fixed_or_pinned = tk.StringVar()

ttk.Label(mainframe, text="Horizontal Spacing Pattern").grid(column=1, row=1, sticky=tk.W)
horizontal_spacing_entry = ttk.Entry(mainframe, width=20, textvariable=horizontal_spacing)
horizontal_spacing_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Vertical Spacing Pattern").grid(column=1, row=2, sticky=tk.W)
vertical_spacing_entry = ttk.Entry(mainframe, width=20, textvariable=vertical_spacing)
vertical_spacing_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Material").grid(column=1, row=3, sticky=tk.W)
material_entry = ttk.Entry(mainframe, width=20, textvariable=material)
material_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Profile").grid(column=1, row=4, sticky=tk.W)
profile_entry = ttk.Entry(mainframe, width=20, textvariable=profile)
profile_entry.grid(column=2, row=4, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Fixed or Pinned").grid(column=1, row=5, sticky=tk.W)
fixed_or_pinned_entry = ttk.OptionMenu(mainframe, fixed_or_pinned, "Fixed", "Pinned")
fixed_or_pinned_entry.grid(column=2, row=5, sticky=(tk.W, tk.E))

generate_button = ttk.Button(mainframe, text="Generate RFEM model", command=generate_model)
generate_button.grid(column=2, row=6, sticky=tk.E)

save_button = ttk.Button(mainframe, text="Save Inputs", command=save_inputs)
save_button = ttk.Button(mainframe, text="Save Inputs", command=save_inputs)
save_button.grid(column=1, row=6, sticky=tk.W)

load_button = ttk.Button(mainframe, text="Load Inputs", command=load_inputs)
load_button.grid(column=1, row=7, sticky=tk.W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

horizontal_spacing_entry.focus()
root.bind('<Return>', generate_model)

style = ttk.Style()
style.configure('Root.TFrame', background='#354F52')
style.configure('Button.TButton', background='#E84C3D', foreground='white')

frame = ttk.Frame(root, style='Root.TFrame')


generate_button = ttk.Button(frame, text="Generate", style='Button.TButton')


save_button = ttk.Button(frame, text="Save", style='Button.TButton')


load_button = ttk.Button(frame, text="Load", style='Button.TButton')


root.mainloop()


'''

This script creates a UI with the specified input fields, 
a drop-down menu for selecting the "Fixed" or "Pinned" option, 
and buttons for "Generating RFEM model", "Loading" inputs from 
a database, and "Saving" inputs to a database. When the 
"Generate RFEM model" button is clicked, the `generate_model` 
function will be called, which currently just outputs a message 
to the console. Similarly, when the "Save Inputs" or "Load Inputs" 
buttons are clicked, the corresponding functions will be called.

Note: The "Loading" and "Saving" functionality is just a placeholder 
for now and will need to be implemented later.

'''
