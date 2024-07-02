import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x400")
# Conversion functions

# Volume conversions
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

# Area conversions
def convert_area(value, from_unit, to_unit):
    conversion_factors = {
        'square meters': 1,
        'square kilometers': 0.000001,
        'square miles': 0.000000386102,
        'acres': 0.000247105
    }
    result = value * conversion_factors[to_unit] / conversion_factors[from_unit]
    return result
# Create and place widgets

# Input field
value_entry = tk.Entry(root)
value_entry.grid(row=0, column=1, padx=10, pady=10)

# Dropdown for unit type
unit_type = tk.StringVar()
unit_type.set("Volume")
unit_type_menu = ttk.Combobox(root, textvariable=unit_type)
unit_type_menu['values'] = ("Volume", "Mass", "Area")
unit_type_menu.grid(row=0, column=2, padx=10, pady=10)

# Dropdowns for from and to units
from_unit = tk.StringVar()
to_unit = tk.StringVar()

from_unit_menu = ttk.Combobox(root, textvariable=from_unit)
to_unit_menu = ttk.Combobox(root, textvariable=to_unit)

from_unit_menu.grid(row=1, column=1, padx=10, pady=10)
to_unit_menu.grid(row=1, column=2, padx=10, pady=10)

# Update unit options based on unit type
def update_units(*args):
    unit_type_selected = unit_type.get()
    if unit_type_selected == "Volume":
        units = ['liters', 'milliliters', 'gallons', 'cubic meters']
    elif unit_type_selected == "Mass":
        units = ['kilograms', 'grams', 'pounds', 'ounces']
    elif unit_type_selected == "Area":
        units = ['square meters', 'square kilometers', 'square miles', 'acres']
    from_unit_menu['values'] = units
    to_unit_menu['values'] = units
    from_unit.set(units[0])
    to_unit.set(units[0])

unit_type.trace('w', update_units)
update_units()

# Conversion button
def convert():
    try:
        value = float(value_entry.get())
        from_u = from_unit.get()
        to_u = to_unit.get()
        unit_type_selected = unit_type.get()

        if unit_type_selected == "Volume":
            result = convert_volume(value, from_u, to_u)
        elif unit_type_selected == "Mass":
            result = convert_mass(value, from_u, to_u)
        elif unit_type_selected == "Area":
            result = convert_area(value, from_u, to_u)

        result_label.config(text=f"Result: {result:.2f} {to_u}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=2, column=1, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=3, column=1, padx=10, pady=10)

# Run the application
root.mainloop()