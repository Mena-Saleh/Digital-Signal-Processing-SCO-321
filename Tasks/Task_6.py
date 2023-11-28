import cmath
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox


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

# Helper functions

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

def load_signal():
    file_path = load_file_path()
    if file_path != -1:
        indices, samples = read_signal(file_path)
    return indices, samples, file_path

def plot_two_signals(indices1,samples1,indices2,samples2, label1, label2):

    plt.figure(figsize=(7, 5))
    plt.subplot(2, 1, 1)
    plt.plot(indices1, samples1, label=label1)
    plt.title(label1)
    plt.xlabel('Index')
    plt.ylabel('Sample Value')
    plt.legend()

    # Plot the smoothed signal
    plt.subplot(2, 1, 2)
    plt.plot(indices2, samples2, label=label2, color='orange')
    plt.title(label2)
    plt.xlabel('Index')
    plt.ylabel('Sample Value')
    plt.legend()
    plt.tight_layout()

    # Show the plots
    plt.show()


# Logic functions
def smoothen_signal(window_size, indices, samples):

    window_size= int(window_size)
    smoothed_samples= []
    smoothed_signal_len= len(samples) - window_size + 1
    for i in range(smoothed_signal_len):
        window = samples[i:i + window_size]
        avg = sum(window) / window_size
        smoothed_samples.append(avg)

    smoothed_indices = range(len(smoothed_samples))
    # Plotting
    plot_two_signals(indices,samples, smoothed_indices ,smoothed_samples, "Original Signal", "Smoothed Signal")

    # Comparing to output
    file_path = load_file_path()
    signal_samples_are_equal(file_path, smoothed_indices, smoothed_samples)

def sharpen_signal(samples):
    first_derivative = []
    second_derivative = []
    for i in range (1, len(samples)):
        first_derivative.append(samples[i] - samples[i-1])
    for i in range (1, len(samples) - 1):
        second_derivative.append(-2 * samples[i] + samples[i-1]  + samples[i+1])


    first_derivative_indices = range(len(first_derivative))
    second_derivative_indices = range(len(second_derivative))

    # Plotting
    plot_two_signals(first_derivative_indices,first_derivative,second_derivative_indices,second_derivative, "First Derivative", "Second Derivative")

    # Comparing to output (Twice, once for each derivative)
    file_path = load_file_path()
    signal_samples_are_equal(file_path, first_derivative_indices, first_derivative)

    file_path = load_file_path()
    signal_samples_are_equal(file_path, second_derivative_indices, second_derivative)

def fold_signal(indices, samples):
    # Assumes the list is symmetrical (I.E zero is in the center)
    folded = samples[::-1]

    # Plotting
    plot_two_signals(indices,samples,indices,folded, "Original Sample", "Folded Sample")

    # Comparing to output (Twice, once for each derivative)
    file_path = load_file_path()
    signal_samples_are_equal(file_path, indices, folded)


def shift_signal(indices, samples, const):
    shifted = [index - float(const) for index in indices]
    print(shifted)
    # Plotting
    plot_two_signals(indices,samples,shifted, samples, "Original Sample", "Shifted Sample")

    # Comparing to output (Twice, once for each derivative)
    file_path = load_file_path()
    signal_samples_are_equal(file_path, shifted, samples, isShiftOp=True)


# Main function

def do_operation(operation, user_input, is_fold= False):
    if operation == "":
        messagebox.showerror("error", "please select an operation")
        return
    indices, samples, file_path = load_signal()

    # Smoothing
    if operation == "Smoothing":
        smoothen_signal(user_input, indices, samples)
    elif operation == "Sharpening":
        sharpen_signal(samples)
    elif operation == "Folding":
        fold_signal(indices, samples)
    elif operation == "Delaying":
        if is_fold:
            samples = samples[::-1]
        shift_signal(indices, samples, -1 *  float(user_input))
    elif operation == "Advancing":
        if is_fold:
            samples = samples[::-1]
        shift_signal(indices, samples, float(user_input))



    

