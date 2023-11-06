import tkinter as tk
from tkinter import ttk 
from Tasks import Task_1 as tsk1
from Tasks import Task_2 as tsk2
from Tasks import Task_3 as tsk3
from Tasks import Task_4 as tsk4
# Functions and styling

def on_enter(e):
    e.widget['background'] = colors["indigo"]  # Change color on hover

def on_leave(e):
    e.widget['background'] = colors["blue"]  # Change color back on mouse leave

# Other windows

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

def open_signal_operations_window():
    op_win = tk.Toplevel(root)
    op_win.title("Signal Operations")
    op_win.geometry("400x360")
    op_win.iconbitmap("Utils/Signaly.ico")


    widget_width = 20

    # Label for selecting operation
    operations_label = tk.Label(op_win, text="Select an Operation:")
    operations_label.grid(row=0, column=0, padx=30, pady=(50,10), sticky="e")
    
    # Combobox for operations
    cmb_operations = ttk.Combobox(op_win, values=["Addition", "Subtraction", "Multiplication", "Squaring", 
                                                 "Shifting", "Normalization", "Accumulation"], width=widget_width-3)
    cmb_operations.grid(row=0, column=1, padx=30, pady=(50,10))

    # Label for selecting normalization type
    normalization_label = tk.Label(op_win, text="Normalization Type:")
    normalization_label.grid(row=1, column=0, padx=30, pady=10, sticky="e")
    
    # Combobox for normalization type
    cmb_normalization = ttk.Combobox(op_win, values=["0 to 1", "-1 to 1"], width=widget_width-3)
    cmb_normalization.grid(row=1, column=1, padx=30, pady=10)

    # Label and Entry for multiplication constant
    multiplication_label = tk.Label(op_win, text="Multiplication Constant:")
    multiplication_label.grid(row=2, column=0, padx=30, pady=10, sticky="e")
    txt_multiplication = tk.Entry(op_win, width=widget_width)
    txt_multiplication.grid(row=2, column=1, padx=30, pady=10)

    # Label and Entry for shifting value
    shifting_label = tk.Label(op_win, text="Shifting Value:")
    shifting_label.grid(row=3, column=0, padx=30, pady=10, sticky="e")
    txt_shifting = tk.Entry(op_win, width=widget_width)
    txt_shifting.grid(row=3, column=1, padx=30, pady=10)


    # Buttons
    btn_operate = tk.Button(op_win, text="Do Operation", bg=colors["blue"], fg=colors["white"], width=15, height=2, relief="flat", bd=0)
    btn_operate.grid(row=4, column=0, padx=(50,30), pady=(40,20), sticky="e")

    btn_compare_output = tk.Button(op_win, text="Compare Output", bg=colors["blue"], fg=colors["white"], width=15, height=2, relief="flat", bd=0)
    btn_compare_output.grid(row=4, column=1, padx=30, pady=(40,20), sticky="e")

    # Button functions
    btn_operate.config(command=lambda:tsk2.do_operation(cmb_operations.get(), txt_shifting.get(), cmb_normalization.get(), txt_multiplication.get(), False))
    btn_compare_output.config(command=lambda:tsk2.do_operation(cmb_operations.get(), txt_shifting.get(), cmb_normalization.get(), txt_multiplication.get(), True))

    # Hover effects
    btn_operate.bind("<Enter>", on_enter)
    btn_operate.bind("<Leave>", on_leave)

def open_signal_quantization_window():
    quant_win = tk.Toplevel(root)
    quant_win.title("Signal Quantization")
    quant_win.geometry("400x300")
    
    widget_width = 20

    # Input label and text box
    input_label = tk.Label(quant_win, text="Input:")
    input_label.grid(row=0, column=0, padx=30, pady=20, sticky="w")
    
    input_textbox = tk.Entry(quant_win, width=widget_width)
    input_textbox.grid(row=0, column=1, padx=10, pady=20, sticky="w")

    # Quantize by label
    quantize_by_label = tk.Label(quant_win, text="Quantize by:")
    quantize_by_label.grid(row=1, column=0, padx=30, pady=5, sticky="w")
    

    # Radio buttons for "Number of bits" and "Number of levels"
    radio_var = tk.IntVar()
    radio_var.set(1)
    
    radio_bits = tk.Radiobutton(quant_win, text="Number of bits", variable=radio_var, value=1)
    radio_bits.grid(row=2, column=0, padx=30, pady=10, sticky="w")
    
    radio_levels = tk.Radiobutton(quant_win, text="Number of levels", variable=radio_var, value=0)
    radio_levels.grid(row=3, column=0, padx=30, pady=10, sticky="w")

    
    # Quantize Signal button
    btn_quantize = tk.Button(quant_win, text="Quantize Signal", bg=colors["blue"], fg=colors["white"], width=15, height=2, relief="flat", bd=0)
    btn_quantize.grid(row=4, column=0, columnspan=2, pady=20)


    # Button functions
    btn_quantize.config(command=lambda: tsk3.quantize_signal(input_textbox.get(), radio_var.get()))


    # Hover effects
    btn_quantize.bind("<Enter>", on_enter)
    btn_quantize.bind("<Leave>", on_leave)


def open_freq_domain_window():
    quant_win = tk.Toplevel(root)
    quant_win.title("freq domain")
    quant_win.geometry("400x300")

    widget_width = 20

    input_label = tk.Label(quant_win, text="Sampling frequency:")
    input_label.grid(row=0, column=0, padx=30, pady=20, sticky="w")

    input_textbox = tk.Entry(quant_win, width=widget_width)
    input_textbox.grid(row=0, column=1, padx=10, pady=20, sticky="w")

    radio_var = tk.IntVar()
    radio_var.set(1)

    radio_dft = tk.Radiobutton(quant_win, text="DFT", variable=radio_var, value=1)
    radio_dft.grid(row=2, column=0, padx=30, pady=10, sticky="w")

    radio_idft = tk.Radiobutton(quant_win, text="IDFT", variable=radio_var, value=0)
    radio_idft.grid(row=3, column=0, padx=30, pady=10, sticky="w")

    btn_load = tk.Button(quant_win, text="browse signal", bg=colors["blue"], fg=colors["white"], width=15,
                             height=2, relief="flat", bd=0)
    btn_load.grid(row=4, column=0, columnspan=2, pady=20)

    # Button functions
    btn_load.config(command=lambda: tsk4.freq_domain(input_textbox.get(), radio_var.get()))

    # Hover effects
    btn_load.bind("<Enter>", on_enter)
    btn_load.bind("<Leave>", on_leave)


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

btn_signal_operations = tk.Button(nav_frame, text="Signal Operations", bg=colors["blue"], fg=colors["white"], width=15, height=2, relief="flat", bd=0)
btn_signal_operations.pack(pady=10, padx=10)

btn_signal_quantization = tk.Button(nav_frame, text="Signal Quantization", bg=colors["blue"], fg=colors["white"], width=15, height=2, relief="flat", bd=0)
btn_signal_quantization.pack(pady=10, padx=10)

btn_freq_domain = tk.Button(nav_frame, text="Frequency Domain", bg=colors["blue"], fg=colors["white"], width=15, height=2, relief="flat", bd=0)
btn_freq_domain.pack(pady=10, padx=10)


# Hover effects
btn_browse.bind("<Enter>", on_enter)
btn_browse.bind("<Leave>", on_leave)

btn_generate.bind("<Enter>", on_enter)
btn_generate.bind("<Leave>", on_leave)

btn_signal_operations.bind("<Enter>", on_enter)
btn_signal_operations.bind("<Leave>", on_leave)

btn_signal_quantization.bind("<Enter>", on_enter)
btn_signal_quantization.bind("<Leave>", on_leave)

btn_freq_domain.bind("<Enter>", on_enter)
btn_freq_domain.bind("<Leave>", on_leave)

# Buttons functions

btn_browse.config(command = tsk1.browse_signal)
btn_generate.config(command=open_generate_signal_window)
btn_signal_operations.config(command=open_signal_operations_window)
btn_signal_quantization.config(command=open_signal_quantization_window)
btn_freq_domain.config(command=open_freq_domain_window)



# Start the Tkinter loop
root.mainloop()

    
