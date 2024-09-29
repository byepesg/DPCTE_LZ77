# compression_project/algorithms/lz77.py
from .compression_algorithm import CompressionAlgorithm

class LZ77(CompressionAlgorithm):
    def __init__(self, window_size, lookahead_buffer_size=15):
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size

    def compress(self, data, window):
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
        decompressed_data = bytearray()

        for match_distance, match_length, next_char in compressed_data:
            if match_length > 0:
                start_index = len(decompressed_data) - match_distance
                decompressed_data.extend(decompressed_data[start_index:start_index + match_length])

            if next_char:
                decompressed_data.extend(next_char)

        return bytes(decompressed_data)
