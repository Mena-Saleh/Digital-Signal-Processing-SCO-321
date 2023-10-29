from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from tkinter import messagebox
import random

# Evaluation function (given):

def signal_samples_are_equal(file_name,indices,samples, isShiftOp = False):
    expected_indices=[]
    expected_samples=[]
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V1=int(L[0])
                V2=float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
                
    if len(expected_samples)!=len(samples):
        print("Test case failed, your signal have different length from the expected one")
        messagebox.showwarning("Test case failed", "your signal have different length from the expected one")
        return
    
    if (isShiftOp):
        to_compare = indices
        to_compare_to = expected_indices
    else:
        to_compare = samples
        to_compare_to = expected_samples
    for i in range(len(to_compare)):
        if abs(to_compare[i] - to_compare_to[i]) < 0.01:
            continue
        else:
            print("Test case failed, your signal have different values from the expected one") 
            messagebox.showwarning("Test case failed", "your signal have different values from the expected one")

            return
    print("Test case passed successfully")
    messagebox.showinfo("Test case succeeded", "Test case passed successfully")

# Helper functions:

def load_file_path():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path != "":
        return file_path
    else:
        return -1

def read_signal(file_path):
    indices = []
    samples = []

    with open(file_path, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = float(L[1])
                indices.append(V1)
                samples.append(V2)
                line = f.readline()
            else:
                break

    return indices, samples

def plot_signals(indices_1, samples_1, indices_2,samples_2, result_indices , result_sample, operation):
    
    plt.figure(figsize=(8, 6))
    plt.plot(indices_1, samples_1, label = "Signal 1", color='red')
    if (samples_2 != 0):
        plt.plot(indices_2, samples_2, label = "Signal 2",  color='blue')
    plt.plot(result_indices, result_sample, label = "Result", color='green')
    plt.title(operation)
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_multiple_signals(list_of_indices, list_of_samples, result_indices, result_sample, operation):
    
    plt.figure(figsize=(8, 6))
    for i in range(len(list_of_samples)):
        random_color = (random.random(), random.random(), random.random())  # Random RGB color
        plt.plot(list_of_indices[i], list_of_samples[i], label=f"Signal {i+1}", color=random_color)
    plt.plot(result_indices, result_sample, label="Result", color='green')
    plt.title(operation)
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()

def load_one_signal():
    file_path1 = load_file_path()
    if file_path1 != -1:
        indices_1, samples_1 = read_signal(file_path1)
    return indices_1, samples_1

def load_two_signals():

    # Read two signals
    file_path1 = load_file_path()
    if file_path1 != -1:
        indices_1, samples_1 = read_signal(file_path1)
    file_path2 = load_file_path()
    if file_path2 != -1:
        indices_2, samples_2 = read_signal(file_path2)

    # Check if the two signals have the same length
    if len(samples_1) != len(samples_2):
        messagebox.showerror("Error", "The two signals must have the same length.")
        return
    return indices_1, samples_1, indices_2, samples_2
        
def load_multiple_file_paths():
    file_paths = filedialog.askopenfilenames(defaultextension=".txt",
                                              filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    return file_paths

def load_multiple_signals():
    file_paths = load_multiple_file_paths()

    if not file_paths:
        return

    list_of_indices = []
    list_of_samples = []

    for file_path in file_paths:
        indices, samples = read_signal(file_path)
        list_of_indices.append(indices)
        list_of_samples.append(samples)

    if (len(list_of_indices) < 2):
        messagebox.showerror("Error", "Must be at least two signals.")
        return
    if len(set(len(samples) for samples in list_of_samples)) != 1:
        messagebox.showerror("Error", "All signals must have the same length.")
        return

    return list_of_indices, list_of_samples

# Operation functions:

def add_signals(list_of_samples):
    return [sum(samples) for samples in zip(*list_of_samples)]

def subtract_signals(samples_1, samples_2):
    result = [s1 - s2 for s1, s2 in zip(samples_1, samples_2)]
    return result

def multiply_signal(samples, const):
    result = [sample * float(const) for sample in samples] 
    return result

def square_signal(samples):
    result = [sample **2 for sample in samples] 
    return result

def shift_signal(indices, const):
    result = [index - float(const) for index in indices]
    return result

def normalize_signal(samples, from_0_to_1):
    if from_0_to_1:
        result = [(sample - min(samples)) / (max(samples) - min(samples)) for sample in samples]
    else:
        result = [2* ((sample - min(samples)) / (max(samples) - min(samples))) - 1 for sample in samples]
    return result

def accumulate_signal(samples):
    result = samples
    for i in range(1, len(samples)):
        samples[i] = samples[i] + samples[i-1]
    return result



# Main function that groups all functions:

def do_operation(operation, shifting_value, normalization_type, multiplication_constant, isCompare = False):
    if operation == "":
        messagebox.showerror("Error", "Please choose an operation.")
        return
    
    if operation == "Subtraction": 

        indices_1, samples_1, indices_2, samples_2 = load_two_signals()

        result_samples = subtract_signals(samples_1, samples_2)
        
        if(isCompare):
            file_path = load_file_path()
            signal_samples_are_equal(file_path, 0, result_samples)
        else:
            plot_signals(indices_1, samples_1, indices_2, samples_2, indices_1, result_samples, operation)

    elif operation == 'Addition':

        list_of_indices, list_of_samples = load_multiple_signals()
        result_samples = add_signals(list_of_samples)
        
        if(isCompare):
            file_path = load_file_path()
            signal_samples_are_equal(file_path, 0, result_samples)
        else:
            plot_multiple_signals(list_of_indices, list_of_samples, list_of_indices[0] , result_samples, operation)


    else:
        indices, samples = load_one_signal()

        if operation == "Squaring":
            result_samples = square_signal(samples)

        elif operation == "Multiplication":

            if(multiplication_constant == ""):
                messagebox.showerror("Error", "Multiplication constant required.")
                return
            result_samples = multiply_signal(samples, multiplication_constant)

        # Special operation on indices rather than samples
        elif operation == "Shifting":
            if(shifting_value == ""):
                messagebox.showerror("Error", "Shifting value required.")
                return
            result_indices = shift_signal(indices, shifting_value)

            if(isCompare):
                file_path = load_file_path()
                signal_samples_are_equal(file_path, result_indices, samples, isShiftOp=True)
            else:
                plot_signals(indices, samples, 0, 0, result_indices, samples, operation)

            return


        elif operation == "Normalization":
            if(normalization_type == ""):
                messagebox.showerror("Error", "Normalization type required.")
                return
            result_samples = normalize_signal(samples, normalization_type == "0 to 1")


        elif operation == "Accumulation":
            result_samples = accumulate_signal(samples)


        if(isCompare):
            file_path = load_file_path()
            signal_samples_are_equal(file_path, 0, result_samples)
        else:
            plot_signals(indices, samples, 0, 0, indices, result_samples, operation)

  
