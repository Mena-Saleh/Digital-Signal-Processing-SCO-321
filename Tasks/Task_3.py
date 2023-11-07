from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from tkinter import messagebox
import random
import math

# Test functions (given)

def QuantizationTest1(file_name,Your_EncodedValues,Your_QuantizedValues):
    expectedEncodedValues=[]
    expectedQuantizedValues=[]
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
                V2=str(L[0])
                V3=float(L[1])
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                line = f.readline()
            else:
                break
    if( (len(Your_EncodedValues)!=len(expectedEncodedValues)) or (len(Your_QuantizedValues)!=len(expectedQuantizedValues))):
        print("QuantizationTest1 Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_EncodedValues)):
        if(Your_EncodedValues[i]!=expectedEncodedValues[i]):
            print("QuantizationTest1 Test case failed, your EncodedValues have different EncodedValues from the expected one") 
            return
    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print("QuantizationTest1 Test case failed, your QuantizedValues have different values from the expected one") 
            return
    print("QuantizationTest1 Test case passed successfully")
    messagebox.showinfo("success", "Test case passed successfully")

def QuantizationTest2(file_name,Your_IntervalIndices,Your_EncodedValues,Your_QuantizedValues,Your_SampledError):
    expectedIntervalIndices=[]
    expectedEncodedValues=[]
    expectedQuantizedValues=[]
    expectedSampledError=[]
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L=line.strip()
            if len(L.split(' '))==4:
                L=line.split(' ')
                V1=int(L[0])
                V2=str(L[1])
                V3=float(L[2])
                V4=float(L[3])
                expectedIntervalIndices.append(V1)
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                expectedSampledError.append(V4)
                line = f.readline()
            else:
                break
    if(len(Your_IntervalIndices)!=len(expectedIntervalIndices)
     or len(Your_EncodedValues)!=len(expectedEncodedValues)
      or len(Your_QuantizedValues)!=len(expectedQuantizedValues)
      or len(Your_SampledError)!=len(expectedSampledError)):
        print("QuantizationTest2 Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_IntervalIndices)):
        if(Your_IntervalIndices[i]!=expectedIntervalIndices[i]):
            print("QuantizationTest2 Test case failed, your signal have different indicies from the expected one") 
            return
    for i in range(len(Your_EncodedValues)):
        if(Your_EncodedValues[i]!=expectedEncodedValues[i]):
            print("QuantizationTest2 Test case failed, your EncodedValues have different EncodedValues from the expected one") 
            return
        
    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print("QuantizationTest2 Test case failed, your QuantizedValues have different values from the expected one") 
            return
    for i in range(len(expectedSampledError)):
        if abs(Your_SampledError[i] - expectedSampledError[i]) < 0.01:
            continue
        else:
            print("QuantizationTest2 Test case failed, your SampledError have different values from the expected one") 
            return
    print("QuantizationTest2 Test case passed successfully")
    messagebox.showinfo("success", "Test case passed successfully")


# Helper functions

def load_file_path():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path != "":
        return file_path
    else:
        return -1

def read_signal(file_path):
    indices=[]
    samples=[]

    with open(file_path, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V1=int(L[0])
                V2=float(L[1])
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
    return indices, samples

def plot_signal(indices, samples):

    plt.figure(figsize=(6, 6)) 

    # Scatter plot
    plt.scatter(indices, samples) 

    # Draw vertical lines from each point to the x-axis
    plt.vlines(indices, 0, samples, linestyles='dashed')

    plt.title("Discrete Form")
    plt.xlabel("Sample Index")
    plt.ylabel("Quantized Amplitude")
    plt.grid(True)

    plt.show()

# Main functions
def quantize_signal(user_input, is_bits):
    indices, signal = load_signal()
    user_input = int(user_input)

    # Step 1: Find min and max amplitude
    min_val = min(signal)
    max_val = max(signal)
    if is_bits==True:
        num_levels = 2 ** user_input
        num_bits = int(user_input)
    else:
        num_levels=user_input
        num_bits = int(math.log2(user_input))

    # Step 2: Find delta
    delta = (max_val - min_val) / num_levels

    # Step 3: Make ranges
    ranges = np.linspace(min_val, max_val, num_levels + 1)

    print(ranges, "\n")

    # Step 4: Calculate mid point for each range
    mid_points = ranges[:-1] + delta / 2

    # Step 5: Quantize
    quantized_signal = np.zeros_like(signal)
    interval_numbers = np.zeros_like(signal)
    for i in range(len(signal)):
        interval_number = np.argmin(np.abs(mid_points - signal[i]))
        quantized_signal[i] = mid_points[interval_number]
        interval_numbers[i] = int(interval_number + 1)

    # Step 6: Calculate error
    error = quantized_signal - signal

    # Step 7: Encode interval numbers to binary
    binary_encoded_intervals = [format(int(interval) - 1, '0' + str(num_bits) + 'b') for interval in interval_numbers]

    # Print results
    print("Range index:", interval_numbers, "\n")
    print("Quantized signal:", quantized_signal, "\n")
    print("Quantization error:", error, "\n")
    print("Binary encoding:", binary_encoded_intervals, "\n")

    # Plot quantized signal
    plot_signal(indices, quantized_signal)

    # Comparing results to output file
    file_path = load_file_path()
    if (is_bits):
        QuantizationTest1(file_path,binary_encoded_intervals, quantized_signal)
    else:
        QuantizationTest2(file_path, interval_numbers, binary_encoded_intervals, quantized_signal, error) 

    return quantized_signal, error, interval_numbers, binary_encoded_intervals

