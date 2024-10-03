# compression_project/main.py
import os
from CompressionAlgorithms.lz77 import LZ77
from utils.file_operations import get_algorithm
from DifferentialPrivacy.LaplaceMechanism import LaplaceMechanism
from Plotting.plot import plot
import numpy as np
import math
import matplotlib.pyplot as plt
class CompressionAlgorithms:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def compress_file(self, input_file_path, output_file_path):
        chunk_size = 1024 * 1024  # Process 1MB at a time
        window = b""
        with open(input_file_path, 'rb') as infile, open(output_file_path, 'w') as outfile:
            while True:
                chunk = infile.read(chunk_size)
                if not chunk:
                    break
                compressed_data, window = self.algorithm.compress(chunk, window)
                for item in compressed_data:
                    outfile.write(f"{item}\n")

    def decompress_file(self, input_file_path, output_file_path):
        compressed_data = []
        with open(input_file_path, 'r') as infile:
            for line in infile:
                compressed_data.append(eval(line.strip()))

        decompressed_data = self.algorithm.decompress(compressed_data)

        with open(output_file_path, 'wb') as outfile:
            outfile.write(decompressed_data)

if __name__ == "__main__":
    algorithm_name = input("Type your algorithm: ").strip().lower()
    algorithm = get_algorithm(algorithm_name)
    
    compression_system = CompressionAlgorithms(algorithm)
    
    choice = input("Enter 'c' for compression or 'd' for decompression: ").strip().lower()
    input_file_name = input("Input file name: ")
    input_file_name_changed = input("Input file name changed: ")
    output_file_name = input("Output file name: ")
    output_file_name_changed = input("Output file name changed: ")

    input_file_path = os.path.join("Input", input_file_name)
    input_file_changed_path = os.path.join("Input", input_file_name_changed)
    file_input_size = os.path.getsize(input_file_path)
    file_input_changed_size = os.path.getsize(input_file_changed_path)

    output_file_path = os.path.join("Output", output_file_name)
    output_file_changed_path = os.path.join("Output", output_file_name_changed)
    

    if choice == 'c':
        compression_system.compress_file(input_file_path, output_file_path)
        compression_system.compress_file(input_file_changed_path, output_file_changed_path)
        file_output_size = os.path.getsize(output_file_path)
        file_output_changed_size = os.path.getsize(output_file_changed_path)
        

    elif choice == 'd':
        compression_system.decompress_file(input_file_path, output_file_path)
        compression_system.decompress_file(input_file_changed_path, output_file_changed_path)
    else:
        print("Invalid choice.")

    print(f"Input file size: {file_input_size} bytes")
    print(f"Input file changed size: {file_input_changed_size} bytes")
    print(f"Output file size: {file_output_size} bytes")
    print(f"Output file changed size: {file_output_changed_size} bytes")
   
    global_sensitivity = file_input_size**(2/3)*np.log(file_input_size)
    store_values = [
        {
            "global_sensitivity": global_sensitivity, 
            "file_output_size": file_output_size, 
            "file_output_changed_size": file_output_changed_size
        }
    ]
    LMw= LaplaceMechanism(epsilon=1,delta=1,n_value=file_input_size).expectedValuePadLength()
    

    # Parameters and noise
    n_values = np.arange(1, file_input_size)  
    epsilon_values = np.array([0.1,0.5,1.0])
    delta_values = np.array([10**-10,10**-7,10**-5])

    for epsilon in epsilon_values:
        for delta in delta_values:
            LaplaceMechanism(epsilon=epsilon,delta=delta,n_value=file_input_changed_size**(2/3)*np.log(file_input_size)).expectedValuePadLength()    
            
            expected_value = np.array([LaplaceMechanism(epsilon=epsilon,delta=delta,n_value=n).expectedValuePadLength() for n in n_values])
            print(f"Expected value: {expected_value}", f"n: {n_values}"), f"epsilon: {epsilon}", f"delta: {delta}"
            plot(n_values,expected_value,"n", "k+e^(-eps)*delta*(1-k))/n",f"Delta:{delta}, Epsilon:{epsilon}","Expected Value(PadLength) vs n",store_values) 
            
    plt.show()        
            
    
    

    # compute pad_lenght/n
    


    
    
    
