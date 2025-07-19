import tkinter as tk
from tkinter import messagebox
import json

# 🔍 Load periodic table data from local JSON file
with open("elements.json", encoding="utf-8") as f:
    element_data = json.load(f)["elements"]

# 🔎 Search element by name
def get_element(name):
    for el in element_data:
        if el['name'].lower() == name.lower():
            return el
    return None

# 🧠 Format element info
def format_info(element):
    info = f"""
Name: {element['name']}
Symbol: {element['symbol']}
Atomic Number: {element['number']}
Atomic Mass: {element['atomic_mass']}
Category: {element.get('category', 'Unknown')}
Phase: {element.get('phase', 'Unknown')}
Boiling Point: {element.get('boil', 'N/A')}
Melting Point: {element.get('melt', 'N/A')}
Shells: {element.get('shells', [])}
Electron Configuration: {element.get('electron_configuration', 'N/A')}
"""
    return info

# 🎨 GUI Setup
def search_element():
    name = entry.get().strip().capitalize()
    if not name:
        messagebox.showwarning("Empty Input", "Please enter an element name.")
        return

    result_box.delete("1.0", tk.END)
    element = get_element(name)
    if element:
        result_box.insert(tk.END, format_info(element))
    else:
        result_box.insert(tk.END, "❌ Element not found. Please check the spelling.")

# 🖼️ GUI
root = tk.Tk()
root.title("🧪 Offline Chemistry Assistant")
root.geometry("600x500")

title = tk.Label(root, text="Enter Element Name:", font=("Arial", 14))
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack()

search_btn = tk.Button(root, text="Search", font=("Arial", 12), command=search_element)
search_btn.pack(pady=5)

result_box = tk.Text(root, font=("Courier", 12), wrap=tk.WORD)
result_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
