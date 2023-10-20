import tkinter as tk
from tkinter import ttk 
from Tasks import Task_1 as tsk1
from  Tasks import  Task2 as tsk2
# Functions and styling

def on_enter(e):
    e.widget['background'] = colors["indigo"]  # Change color on hover

def on_leave(e):
    e.widget['background'] = colors["blue"]  # Change color back on mouse leave

def open_generate_signal_window():
    gen_win = tk.Toplevel(root)
    gen_win.title("Generate Signals")
    gen_win.geometry("400x360")
    gen_win.iconbitmap("Utils/Signaly.ico")
    
    widget_width = 20
    
    # Input fields
    lbl_amplitude = tk.Label(gen_win, text="Amplitude:")
    lbl_amplitude.grid(row=0, column=0, padx=30, pady=(50,10), sticky="e")
    txt_amplitude = tk.Entry(gen_win, width=widget_width)
    txt_amplitude.grid(row=0, column=1, padx=30, pady=(50,10))
    
    lbl_wave_type = tk.Label(gen_win, text="Wave Type:")
    lbl_wave_type.grid(row=1, column=0, padx=30, pady=10, sticky="e")
    cmb_wave_type = ttk.Combobox(gen_win, values=["sin", "cos"], width=widget_width - 3)
    cmb_wave_type.grid(row=1, column=1, padx=30, pady=10)
    
    lbl_analog_freq = tk.Label(gen_win, text="Analogue Frequency:")
    lbl_analog_freq.grid(row=2, column=0, padx=30, pady=10, sticky="e")
    txt_analog_freq = tk.Entry(gen_win, width=widget_width)
    txt_analog_freq.grid(row=2, column=1, padx=30, pady=10)
    
    lbl_sampling_freq = tk.Label(gen_win, text="Sampling Frequency:")
    lbl_sampling_freq.grid(row=3, column=0, padx=30, pady=10, sticky="e")
    txt_sampling_freq = tk.Entry(gen_win, width=widget_width)
    txt_sampling_freq.grid(row=3, column=1, padx=30, pady=10)
    
    lbl_phase_shift = tk.Label(gen_win, text="Phase Shift:")
    lbl_phase_shift.grid(row=4, column=0, padx=30, pady=10, sticky="e")
    txt_phase_shift = tk.Entry(gen_win, width=widget_width)
    txt_phase_shift.grid(row=4, column=1, padx=30, pady=10)

    # Buttons
    btn_generate_signal = tk.Button(gen_win, text="Generate Signal", bg=colors["blue"], fg=colors["white"], width=15, height=2, relief="flat", bd=0)
    btn_generate_signal.grid(row=5, column=0, padx=(50,30), pady=(40,20), sticky="e")

    btn_compare_output = tk.Button(gen_win, text="Compare Output", bg=colors["blue"], fg=colors["white"], width=15, height=2, relief="flat", bd=0)
    btn_compare_output.grid(row=5, column=1, padx=30, pady=(40,20), sticky="e")

    # Hover effects
    btn_generate_signal.bind("<Enter>", on_enter)
    btn_generate_signal.bind("<Leave>", on_leave)

    btn_compare_output.bind("<Enter>", on_enter)
    btn_compare_output.bind("<Leave>", on_leave)

    # Buttons functions

    btn_generate_signal.config(command=lambda: tsk1.generate_signal(txt_amplitude.get(), cmb_wave_type.get(), 
                                                                    txt_analog_freq.get(),txt_sampling_freq.get(), txt_phase_shift.get()))
    
    btn_compare_output.config(command=lambda: tsk1.compare_outputs(txt_amplitude.get(), cmb_wave_type.get(), 
                                                                    txt_analog_freq.get(),txt_sampling_freq.get(), txt_phase_shift.get()))

    btn_compare_output.config(command=lambda: tsk1.compare_outputs(txt_amplitude.get(), cmb_wave_type.get(),
                                                                   txt_analog_freq.get(), txt_sampling_freq.get(),
                                                                   txt_phase_shift.get()))

   # btn_operate.config(command=lambda: tsk2.do_operation()
# Color palette
colors = {
    "champagne": "#F2DFD7",
    "white": "#FEF9FF",
    "thistle": "#D4C1EC",
    "indigo": "#9F9FED",
    "blue": "#736CED",
}

# Main window setup
root = tk.Tk()
root.title("Signaly")
root.geometry("800x600")
root.resizable(False, False)
root.iconbitmap("Utils/Signaly.ico")


# Navigation frame
nav_frame = tk.Frame(root, bg=colors["thistle"])
nav_frame.pack(side="left", fill="y")


# Navigation buttons
btn_browse = tk.Button(nav_frame, text="Browse Signals", bg=colors["blue"], fg=colors["white"], width=15, height=2, relief="flat", bd=0)
btn_browse.pack(pady=(40,10), padx=10)

btn_generate = tk.Button(nav_frame, text="Generate Signals", bg=colors["blue"], fg=colors["white"], width=15, height=2, relief="flat", bd=0)
btn_generate.pack(pady=10, padx=10)

operations_label = tk.Label(nav_frame, text="Select Operation",bg='gray', fg=colors["white"])
operations_label.pack( padx=(10,10), pady=(30,0))
cmb_operations = ttk.Combobox(nav_frame, values=["addition", "subtraction", "multiplication ","Squaring", "Shifting",
                                                 "Normalization","Accumulation "], width=15)
cmb_operations.pack(pady=10)

btn_operate = tk.Button(nav_frame, text="ok", bg=colors["blue"], fg=colors["white"], width=8, height=1, relief="flat", bd=0)
btn_operate.pack(pady=5, padx=5)



# Hover effects
btn_browse.bind("<Enter>", on_enter)
btn_browse.bind("<Leave>", on_leave)

btn_generate.bind("<Enter>", on_enter)
btn_generate.bind("<Leave>", on_leave)

btn_operate.bind("<Enter>", on_enter)
btn_operate.bind("<Leave>", on_leave)

# Buttons functions
btn_browse.config(command = tsk1.browse_signal)
btn_generate.config(command=open_generate_signal_window)
btn_operate.config(command=lambda: tsk2.do_operation(cmb_operations.get()))

# Start the Tkinter loop
root.mainloop()

    
