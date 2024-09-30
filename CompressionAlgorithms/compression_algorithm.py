# compression_project/algorithms/compression_algorithm.py
from abc import ABC, abstractmethod

class CompressionAlgorithm(ABC):
    @abstractmethod
    def compress(self, data, window):
        pass
    
    @abstractmethod
    def decompress(self, compressed_data):
        pass
