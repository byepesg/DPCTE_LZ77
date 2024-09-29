# compression_project/main.py
import os
from CompressionAlgorithms.lz77 import LZ77
from utils.file_operations import get_algorithm
from DifferentialPrivacy.LaplaceMechanism import LaplaceMechanism
from Plotting.plot import plot
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
    output_file_name = input("Output file name: ")

    input_file_path = os.path.join("Input", input_file_name)
    output_file_path = os.path.join("Output", output_file_name)

    if choice == 'c':
        compression_system.compress_file(input_file_path, output_file_path)
        plot()

    elif choice == 'd':
        compression_system.decompress_file(input_file_path, output_file_path)
    else:
        print("Invalid choice.")
