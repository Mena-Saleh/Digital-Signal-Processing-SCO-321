import tkinter as tk
import Task_1 as tsk1

# Functions
    
# Main window
root = tk.Tk()
root.title("DSP")

# Set window size
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)

# Widgets

# Browse label 
my_label = tk.Label(root, text="Select a signal file to visualize it.")
my_label.pack(padx=20, pady= 20)

# Browse button
my_button = tk.Button(root, text="Browse Signals", command=tsk1.browse_signal)
my_button.pack(padx=20, pady= 20)

# Start the main event loop
root.mainloop()