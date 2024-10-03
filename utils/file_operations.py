# compression_project/utils/file_operations.py
from CompressionAlgorithms.lz77 import LZ77

def get_algorithm(algorithm_name):
    if algorithm_name == 'lz77':
        # return LZ77(window_size=50)
        return LZ77(window_size=50) 
    else:
        raise ValueError(f"Unknown algorithm: {algorithm_name}")
