import os
import ast

class LZ77:
    def __init__(self, window_size, lookahead_buffer_size=15):
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size

    def compress_chunk(self, data, window):
        i = 0
        output = []
        while i < len(data):
            match_distance = 0
            match_length = 0

            for j in range(1, min(self.window_size, len(window)) + 1):
                start_index = j - 1
                length = 0
                while length < self.lookahead_buffer_size and (i + length) < len(data) and (start_index + length) < len(window) and window[start_index + length] == data[i + length]:
                    length += 1
                if length > match_length:
                    match_distance = j - 1
                    match_length = length

            if match_length > 0:
                output.append([match_distance, match_length, data[i + match_length:i + match_length + 1] if i + match_length < len(data) else b''])
                window += data[i:i + match_length + 1]
                i += match_length + 1
            else:
                output.append([0, 0, data[i:i + 1]])
                window += data[i:i + 1]
                i += 1

            if len(window) > self.window_size:
                window = window[-self.window_size:]

        return output, window
    
    def decompress(self, compressed_data):
        decompressed_data = bytearray()  # Use bytearray for mutable bytes

        for match_distance, match_length, next_char in compressed_data:
            if match_length > 0:
                start_index = len(decompressed_data) - match_distance
                decompressed_data.extend(decompressed_data[start_index:start_index + match_length])

            if next_char:
                decompressed_data.extend(next_char)

        return bytes(decompressed_data)  # Convert to immutable bytes at the end

def calculate_window_size(file_size):
    if file_size < 1024 * 1024:  # Less than 1MB
        return 20
    elif file_size < 10 * 1024 * 1024:  # Between 1MB and 10MB
        return 50
    else:  # Greater than 10MB
        return 100

def compress_file():
    input_file_name = input("Enter the name of the input file (with extension): ")
    input_dir = "Input"
    output_dir = "Output"

    input_file_path = os.path.join(input_dir, input_file_name)
    output_file_name = os.path.splitext(input_file_name)[0] + "_compressed.txt"
    output_file_path = os.path.join(output_dir, output_file_name)

    if not os.path.exists(input_file_path):
        print(f"Error: The file '{input_file_name}' does not exist in the 'Input' folder.")
        return

    file_size = os.path.getsize(input_file_path)
    window_size = calculate_window_size(file_size)

    print(f"File size: {file_size} bytes. Using window size: {window_size}.")

    lz77_compressor = LZ77(window_size=window_size)

    chunk_size = 1024 * 1024  # Process 1MB at a time
    window = b""  # Use bytes for the window
    with open(input_file_path, 'rb') as infile, open(output_file_path, 'w') as outfile:  # Open input in binary and output in text mode
        while True:
            chunk = infile.read(chunk_size)
            if not chunk:
                break
            compressed_data, window = lz77_compressor.compress_chunk(chunk, window)
            for item in compressed_data:
                outfile.write(f"{item}\n")  # Write as text

    print(f"Compressed data has been written to '{output_file_path}'.")

def decompress_file():
    input_file_name = input("Enter the name of the compressed file (with extension): ")
    input_dir = "Output"
    output_dir = "Output"

    input_file_path = os.path.join(input_dir, input_file_name)
    output_file_name = os.path.splitext(input_file_name)[0].replace("_compressed", "") + "_decompressed.txt"
    output_file_path = os.path.join(output_dir, output_file_name)

    if not os.path.exists(input_file_path):
        print(f"Error: The file '{input_file_name}' does not exist in the 'Output' folder.")
        return

    lz77_compressor = LZ77(window_size=0)  # Window size is irrelevant for decompression

    compressed_data = []
    with open(input_file_path, 'r') as infile:
        for line in infile:
            compressed_data.append(ast.literal_eval(line.strip()))  # Safely evaluate the string as a list

    decompressed_data = lz77_compressor.decompress(compressed_data)

    with open(output_file_path, 'wb') as outfile:
        outfile.write(decompressed_data)

    print(f"Decompressed data has been written to '{output_file_path}'.")

if __name__ == "__main__":
    choice = input("Enter 'c' to compress a file or 'd' to decompress a file: ").strip().lower()
    if choice == 'c':
        compress_file()
    elif choice == 'd':
        decompress_file()
    else:
        print("Invalid choice. Please enter 'c' to compress or 'd' to decompress.")
