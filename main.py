# compression_project/main.py
import os
from CompressionAlgorithms.lz77 import LZ77
from utils.file_operations import get_algorithm
from DifferentialPrivacy.LaplaceMechanism import LaplaceMechanism
from Plotting.plot import plot
import numpy as np
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
    input_file_name_changed = input("Input file name: ")
    output_file_name = input("Output file name: ")
    output_file_name_changed = input("Output file name: ")

    input_file_path = os.path.join("Input", input_file_name)
    input_file_changed_path = os.path.join("Input", input_file_name)
    file_input_size = os.path.getsize(input_file_path)
    file_input_changed_size = os.path.getsize(input_file_changed_path)

    output_file_path = os.path.join("Output", output_file_name)
    output_file_changed_path = os.path.join("Output", output_file_name)
    file_output_size = os.path.getsize(output_file_path)
    file_output_changed_size = os.path.getsize(output_file_changed_path)

    if choice == 'c':
        compression_system.compress_file(input_file_path, output_file_path)
        compression_system.compress_file(input_file_changed_path, output_file_changed_path)
        

    elif choice == 'd':
        compression_system.decompress_file(input_file_path, output_file_path)
        compression_system.decompress_file(input_file_changed_path, output_file_changed_path)
    else:
        print("Invalid choice.")

    print(f"Input file size: {file_input_size} bytes")
    print(f"Output file size: {file_output_size} bytes")
    print(f"Input file changed size: {file_input_changed_size} bytes")
    print(f"Output file changed size: {file_output_changed_size} bytes")
    print(f"Compression ratio: {file_output_changed_size-file_output_size}")
    global_sensitivity = file_output_changed_size-file_output_size
    store_values=[{global_sensitivity:global_sensitivity}]
    LMw= LaplaceMechanism(global_sensitivity=global_sensitivity,epsilon=1,delta=1,compression=file_input_size).add_noise(1)
    print (f"LM(w): {LMw}")
    LMwp= LaplaceMechanism(global_sensitivity=global_sensitivity,epsilon=1,delta=1,compression=file_input_changed_size).add_noise(1)
    print (f"LM(w'): {LMwp}")
    

    # n-values
    n_values = np.arange(1, file_output_size)  
    n_values_p = np.arange(1, file_output_changed_size) 

    # Compute pad_length for each n value
    pad_length_values = np.array([LaplaceMechanism(global_sensitivity=global_sensitivity,epsilon=1,delta=1,compression=n).add_noise(1) for n in n_values])
    pad_length_values_p = np.array([LaplaceMechanism(global_sensitivity=global_sensitivity,epsilon=1,delta=1,compression=n).add_noise(1) for n in n_values_p])
    # compute pad_lenght/n
    pad_length_per_n = pad_length_values / n_values
    pad_length_per_n_p = pad_length_values_p / n_values
    plot(n_values,pad_length_per_n,pad_length_per_n_p,"n", "pad_length/n","Compress(w): (pad_length)/n vs n","Compress(w'): (pad_length)/n vs n","Compress(w) vs Compress(w')",store_values) 
    
