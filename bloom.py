import math
import mmh3

class BloomFilter:
    def __init__(self, n, p):
        self.n = n  # Number of expected elements
        self.p = p  # False positive probability
        self.m = self.calculate_size(n, p)  # Size of bit array
        self.k = self.calculate_hash_count(self.m, n)  # Number of hash functions
        self.bit_array = [False] * self.m  # Initialize bit array

    def add(self, element):
        for i in range(self.k):
            index = mmh3.hash(element, i) % self.m
            self.bit_array[index] = True

    def __contains__(self, element):
        for i in range(self.k):
            index = mmh3.hash(element, i) % self.m
            if not self.bit_array[index]:
                return False
        return True

    @staticmethod
    def calculate_size(n, p):
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    @staticmethod
    def calculate_hash_count(m, n):
        k = (m / n) * math.log(2)
        return int(k)

# Example usage:
bloom_filter = BloomFilter(1000, 0.01)
bloom_filter.add("hello")
bloom_filter.add("world")
print("hello" in bloom_filter)  # Output: True
print("python" in bloom_filter)  # Output: False (probably)

