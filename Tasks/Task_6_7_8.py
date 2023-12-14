import cmath
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
import math

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

def Shift_Fold_Signal(file_name,Your_indices,Your_samples):      
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
    print("Current Output Test file is: ")
    print(file_name)
    print("\n")
    if (len(expected_samples)!=len(Your_samples)) and (len(expected_indices)!=len(Your_indices)):
        print("Shift_Fold_Signal Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if(Your_indices[i]!=expected_indices[i]):
            print("Shift_Fold_Signal Test case failed, your signal have different indicies from the expected one") 
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Shift_Fold_Signal Test case failed, your signal have different values from the expected one") 
            return
    print("Shift_Fold_Signal Test case passed successfully")

def ConvTest(Your_indices,Your_samples): 
    """
    Test inputs
    InputIndicesSignal1 =[-2, -1, 0, 1]
    InputSamplesSignal1 = [1, 2, 1, 1 ]
    
    InputIndicesSignal2=[0, 1, 2, 3, 4, 5 ]
    InputSamplesSignal2 = [ 1, -1, 0, 0, 1, 1 ]
    """
    
    expected_indices=[-2, -1, 0, 1, 2, 3, 4, 5, 6]
    expected_samples = [1, 1, -1, 0, 0, 3, 3, 2, 1 ]

    
    if (len(expected_samples)!=len(Your_samples)) and (len(expected_indices)!=len(Your_indices)):
        print("Conv Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if(Your_indices[i]!=expected_indices[i]):
            print("Conv Test case failed, your signal have different indicies from the expected one") 
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Conv Test case failed, your signal have different values from the expected one") 
            return
    print("Conv Test case passed successfully")

def CorrTest(file_name,Your_indices,Your_samples):      
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
    print("Current Output Test file is: ")
    print(file_name)
    print("\n")
    if (len(expected_samples)!=len(Your_samples)) and (len(expected_indices)!=len(Your_indices)):
        print("Shift_Fold_Signal Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if(Your_indices[i]!=expected_indices[i]):
            print("Shift_Fold_Signal Test case failed, your signal have different indicies from the expected one") 
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Correlation Test case failed, your signal have different values from the expected one") 
            return
    print("Correlation Test case passed successfully")

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

    # Comparing to output
    file_path = load_file_path()
    signal_samples_are_equal(file_path, indices, folded)

def shift_signal(indices, samples, const):
    shifted = [index - float(const) for index in indices]
    # Plotting
    plot_two_signals(indices,samples,shifted, samples, "Original Sample", "Shifted Sample")

    # Comparing to output
    file_path = load_file_path()
    Shift_Fold_Signal(file_path, shifted, samples)

def convolve_signals(indices1, samples1, indices2, samples2):
    # Get the range of indices and populate a list of indices for the resulting signal
    result_min_index = min(indices1) + min(indices2)
    result_max_index = max(indices1) + max(indices2)
    result_indices = list(range(result_min_index, result_max_index + 1))

    # Initialize an array to hold the samples of the convolved signal
    result_samples = []

    # Go through each index in the result indices
    for i in result_indices:
        # Initialize the sum for this index
        sum_samples = 0
        # Go through each index in the first signal
        for j in indices1:
            # Calculate the corresponding index in the second signal
            k = i - j
            # If k is in the range of indices2, multiply the samples and add to the sum
            # If it is not in range that means its 0 so the sum is 0, so nothing needs to be done.
            if k in indices2:
                sum_samples += samples1[indices1.index(j)] * samples2[indices2.index(k)]

        # Append the calculated sum to the result samples
        result_samples.append(sum_samples)
        
    # Print results
    print("Result indices: ", result_indices)
    print("Result samples: ", result_samples)
    return result_indices, result_samples

def correlate_signals(indices1, samples1, indices2, samples2:list):
    # Initializing indices and populating
    n = len(indices1)
    result_indices =list(range(n)) 
    
    # Calculate denumerator once
    denumerator = 1/n * math.sqrt((sum([i**2 for i in samples1]) * sum([i**2 for i in samples2])))
    # Initializing samples list.
    result_samples = []
    for i in range (n):
        # First iteration there is no shifting, just multiply
        curr_result = sum(s1*s2 for s1,s2 in zip(samples1,samples2))
        numerator = curr_result/n
        result_samples.append(numerator/denumerator)
        # Pop first element in second signal and add it to the end (lag by 1).
        first_element = samples2[0]
        samples2.pop(0)
        samples2.append(first_element)
        
    print("Result signal: ", result_samples)
    
    return result_indices, result_samples

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
    elif operation == "Convolution":
        indices2, samples2, file_path = load_signal()
        result_indices, result_samples = convolve_signals(indices, samples, indices2, samples2)
        ConvTest(result_indices, result_samples)
    elif operation == "Correlation":
        indices2, samples2, file_path = load_signal()
        result_indices, result_samples = correlate_signals(indices, samples, indices2, samples2)
        file_path = load_file_path()
        CorrTest(file_path, result_indices, result_samples)

