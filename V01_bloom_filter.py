import math
import hashlib

class BloomFilter:

    def __init__(self, capacity, error_rate):

        self.capacity = capacity # Número máximo de elementos que podem ser armazenados.
        self.error_rate = error_rate # Taxa máxima de falso positivo desejada.
        self.num_bits = self.get_num_bits(capacity, error_rate) # Número de bits necessários.
        self.num_hashes = self.get_num_hashes(self.num_bits, capacity) # Número de funções de hash necessárias.
        self.bit_array = [0] * self.num_bits # Array de bits para armazenar os elementos. São inicializados com zeros

    def hash_element(self, element, i):
        # Combina o elemento com o índice do hash e gera um hash SHA-256
        data = f"{element}_{i}".encode("utf-8")
        digest = hashlib.sha256(data).hexdigest()
        return int(digest, 16) % self.num_bits
    
    def add(self, element):
        for i in range(self.num_hashes):
            hash_val = self.hash_element(element, i)
            self.bit_array[hash_val] = 1

    def __contains__(self, element):
        for i in range(self.num_hashes):
            hash_val = self.hash_element(element, i)
            if self.bit_array[hash_val] == 0:
                return False
        return True

    def get_num_bits(self, capacity, error_rate):
        num_bits = - (capacity * math.log(error_rate)) / (math.log(2) ** 2)
        return int(num_bits)

    def get_num_hashes(self, num_bits, capacity):
        num_hashes = (num_bits / capacity) * math.log(2)
        return int(num_hashes)

# Exemplo de uso
bloom_filter = BloomFilter(10000, 0.1)


bloom_filter.add("maca")
bloom_filter.add("banana")
bloom_filter.add("melancia")

print("melancia" in bloom_filter)
print("pear" in bloom_filter)
print("orange" in bloom_filter)
print("banana" in bloom_filter)
print("maca" in bloom_filter)
print("laranja" in bloom_filter)
