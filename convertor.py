import tkinter as tk
from tkinter import ttk, messagebox

# Root window setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("420x250")
root.resizable(False, False)

# ==== Conversion functions ====

def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        'liters': 1,
        'milliliters': 1000,
        'gallons': 0.264172,
        'cubic meters': 0.001
    }
    result = value * conversion_factors[to_unit] / conversion_factors[from_unit]
    return result

def convert_mass(value, from_unit, to_unit):
    conversion_factors = {
        'kilograms': 1,
        'grams': 1000,
        'pounds': 2.20462,
        'ounces': 35.274
    }
    result = value * conversion_factors[to_unit] / conversion_factors[from_unit]
    return result

def convert_area(value, from_unit, to_unit):
    conversion_factors = {
        'square meters': 1,
        'square kilometers': 0.000001,
        'square miles': 0.000000386102,
        'acres': 0.000247105
    }
    result = value * conversion_factors[to_unit] / conversion_factors[from_unit]
    return result

# ==== UI Elements ====

# Title Label
title_label = tk.Label(root, text="Multi-Unit Converter", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Value Entry
tk.Label(root, text="Enter Value:").grid(row=1, column=0, sticky="e", padx=10)
value_entry = tk.Entry(root, width=15)
value_entry.grid(row=1, column=1, columnspan=2, pady=5)

# Unit Type Dropdown
tk.Label(root, text="Unit Type:").grid(row=2, column=0, sticky="e", padx=10)
unit_type = tk.StringVar(value="Volume")
unit_type_menu = ttk.Combobox(root, textvariable=unit_type, state="readonly")
unit_type_menu['values'] = ("Volume", "Mass", "Area")
unit_type_menu.grid(row=2, column=1, columnspan=2, pady=5)

# From and To Unit Dropdowns
tk.Label(root, text="From Unit:").grid(row=3, column=0, sticky="e", padx=10)
from_unit = tk.StringVar()
from_unit_menu = ttk.Combobox(root, textvariable=from_unit, state="readonly")
from_unit_menu.grid(row=3, column=1, pady=5)

tk.Label(root, text="To Unit:").grid(row=4, column=0, sticky="e", padx=10)
to_unit = tk.StringVar()
to_unit_menu = ttk.Combobox(root, textvariable=to_unit, state="readonly")
to_unit_menu.grid(row=4, column=1, pady=5)

# ==== Update unit options based on unit type ====
def update_units(*args):
    unit_type_selected = unit_type.get()
    if unit_type_selected == "Volume":
        units = ['liters', 'milliliters', 'gallons', 'cubic meters']
    elif unit_type_selected == "Mass":
        units = ['kilograms', 'grams', 'pounds', 'ounces']
    elif unit_type_selected == "Area":
        units = ['square meters', 'square kilometers', 'square miles', 'acres']
    else:
        units = []

    from_unit_menu['values'] = units
    to_unit_menu['values'] = units
    if units:
        from_unit.set(units[0])
        to_unit.set(units[1] if len(units) > 1 else units[0])

unit_type.trace('w', update_units)
update_units()

# ==== Convert Button Logic ====
def convert():
    try:
        value = float(value_entry.get())
        from_u = from_unit.get()
        to_u = to_unit.get()
        unit_type_selected = unit_type.get()

        if from_u == "" or to_u == "":
            raise ValueError("Units not selected.")

        if unit_type_selected == "Volume":
            result = convert_volume(value, from_u, to_u)
        elif unit_type_selected == "Mass":
            result = convert_mass(value, from_u, to_u)
        elif unit_type_selected == "Area":
            result = convert_area(value, from_u, to_u)
        else:
            raise ValueError("Invalid unit type.")

        result_label.config(text=f"Result: {result:.4f} {to_u}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number and ensure units are selected.")

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert, bg="#4CAF50", fg="white", width=15)
convert_button.grid(row=5, column=1, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="Result: ", font=("Helvetica", 12))
result_label.grid(row=6, column=0, columnspan=3, pady=10)

# Start app
root.mainloop()
