import math
import mmh3  #bib usada para gerar valores de hash

class BloomFilter:

    def __init__(self, capacity, error_rate): # inicializando

        self.capacity = capacity # Número máximo de elementos que podem ser armazenados.
        self.error_rate = error_rate # Taxa máxima de falso positivo desejada.
        self.num_bits = self.get_num_bits(capacity, error_rate) # Número de bits necessários.
        self.num_hashes = self.get_num_hashes(self.num_bits, capacity) # Número de funções de hash necessárias.
        self.bit_array = [0] * self.num_bits # Array de bits para armazenar os elementos. São inicializados com zeros
        
    def add(self, element):
        for i in range(self.num_hashes):
            # Gera um valor de hash para o elemento e define o bit correspondente como 1.
            hash_val = mmh3.hash(element, i) % self.num_bits
            self.bit_array[hash_val] = 1

            # Para cada uma das num_hashes, gera m valor de hash diferente 
        
    def __contains__(self, element):
        for i in range(self.num_hashes):
            # Gera um valor de hash para o elemento e verifica se o bit correspondente é 1.
            hash_val = mmh3.hash(element, i) % self.num_bits
            if self.bit_array[hash_val] == 0:
                # Se algum dos bits for 0, o elemento definitivamente não está presente.
                return False
        # Se todos os bits forem 1, o elemento pode estar presente ou não.
        return True
    
    def get_num_bits(self, capacity, error_rate):
        
        #calcula o número de bits m
        num_bits = - (capacity * math.log(error_rate)) / (math.log(2) ** 2)
        return int(num_bits)
    
    def get_num_hashes(self, num_bits, capacity):

        # minimiza a taxa de erro
        num_hashes = (num_bits / capacity) * math.log(2)
        return int(num_hashes)

bloom_filter = BloomFilter(10000, 0.1) #filtro para armazenar até 10000 elementos com 10% de taxa de erro

# Adicionando elementos no bloom filter
bloom_filter.add("maca")
bloom_filter.add("banana")
bloom_filter.add("laranja")

# check elementos no bloom filter
print("apple" in bloom_filter) # 
print("pear" in bloom_filter) # 
print("orange" in bloom_filter) #
print("banana" in bloom_filter) #
print("maca" in bloom_filter) #
print("laranja" in bloom_filter) #

