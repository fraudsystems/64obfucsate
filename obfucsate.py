import os
import base64
import tkinter as tk
from tkinter import filedialog, messagebox

def obfuscate_code(original_code):
    """Encodes the original code to Base64."""
    return base64.b64encode(original_code.encode()).decode()

def obfuscate_file(input_file, output_file):
    """Obfuscates the input Python file and saves it to the output file."""
    try:
        with open(input_file, 'r') as file:
            original_code = file.read()

        encoded_code = obfuscate_code(original_code)

        with open(output_file, 'w') as file:
            file.write(f"import base64\n")
            file.write(f"exec(base64.b64decode('{encoded_code}'))")
        
        messagebox.showinfo("Success", f"File obfuscated and saved to:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_input_file():
    """Opens a file dialog to select the input Python file."""
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if file_path:
        input_file_var.set(file_path)

def select_output_file():
    """Opens a file dialog to select the output file path."""
    file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py")])
    if file_path:
        output_file_var.set(file_path)

def obfuscate():
    """Obfuscates the selected file and saves the output."""
    input_file = input_file_var.get()
    output_file = output_file_var.get()

    if not input_file or not output_file:
        messagebox.showwarning("Warning", "Please select both input and output files.")
        return

    obfuscate_file(input_file, output_file)

# Create the main window
root = tk.Tk()
root.title("b64 obfuscator")
root.geometry("400x200")
root.configure(bg="#2E2E2E")

# Variables to hold file paths
input_file_var = tk.StringVar()
output_file_var = tk.StringVar()

# Input File Selection
input_frame = tk.Frame(root, bg="#2E2E2E")
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="select py file:", bg="#2E2E2E", fg="#FFFFFF")
input_label.pack(side=tk.LEFT)

input_entry = tk.Entry(input_frame, textvariable=input_file_var, width=40)
input_entry.pack(side=tk.LEFT)

input_button = tk.Button(input_frame, text="Sel", command=select_input_file)
input_button.pack(side=tk.LEFT)

# Output File Selection
output_frame = tk.Frame(root, bg="#2E2E2E")
output_frame.pack(pady=10)

output_label = tk.Label(output_frame, text="output dir:", bg="#2E2E2E", fg="#FFFFFF")
output_label.pack(side=tk.LEFT)

output_entry = tk.Entry(output_frame, textvariable=output_file_var, width=40)
output_entry.pack(side=tk.LEFT)

output_button = tk.Button(output_frame, text="Sel", command=select_output_file)
output_button.pack(side=tk.LEFT)

# Obfuscate Button
obfuscate_button = tk.Button(root, text="Obfuscate", command=obfuscate, bg="#A052BE", fg="#FFFFFF")
obfuscate_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()