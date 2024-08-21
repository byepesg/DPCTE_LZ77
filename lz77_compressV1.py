class LZ77:
    def __init__(self, window_size=20, lookahead_buffer_size=15):
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size

    def compress(self, data):
        i = 0
        output = []
        window = ""

        while i < len(data):
            match_distance = 0
            match_length = 0

            # Search from the earliest to the most recent in the window
            for j in range(1, min(self.window_size, len(window)) + 1):
                start_index = j - 1
                length = 0

                # Ensure we don't exceed the window size during matching
                while length < self.lookahead_buffer_size and (i + length) < len(data) and (start_index + length) < len(window) and window[start_index + length] == data[i + length]:
                    length += 1

                if length > match_length:
                    match_distance = j-1
                    match_length = length

            # If a match is found, store the (distance, length, next character)
            if match_length > 0:
                output.append((match_distance, match_length, data[i + match_length] if i + match_length < len(data) else ''))
                window += data[i:i + match_length + 1]
                i += match_length + 1
            else:
                output.append((0, 0, data[i]))
                window += data[i]
                i += 1

            # Keep the window size within the specified limit
            if len(window) > self.window_size:
                window = window[-self.window_size:]

        return output
    

    

# Test input
input_data = "Hello, world!"

# Create an instance of the LZ77 compressor
lz77_compressor = LZ77()

# Compress the input data
compressed_data = lz77_compressor.compress(input_data)

# Output the compressed data
for item in compressed_data:
    print(item)
