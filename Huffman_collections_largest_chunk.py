import heapq
from collections import defaultdict
from collections import Counter
import math

class Node:
    def __init__(self, value=None, frequency=None):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __le__(self, other):
        return self.frequency <= other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __ge__(self, other):
        return self.frequency >= other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __ne__(self, other):
        return self.frequency != other.frequency

def find_repeated_chunks(binary_sequence):
    max_chunk = ""
    max_length = 0
    max_frequency = 0

    for i in range(len(binary_sequence)):
        for j in range(i + 1, len(binary_sequence)):
            chunk = binary_sequence[i:j]
            frequency = binary_sequence.count(chunk)
            if frequency >= 2 and len(chunk) > max_length:
                max_chunk = chunk
                max_length = len(chunk)
                max_frequency = frequency

    return max_chunk, max_frequency

def build_huffman_tree(chunks):
    heap = [Node(value=chunk, frequency=frequency) for chunk, frequency in chunks.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(frequency=left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]

def generate_huffman_codes(node, prefix='', codes={}):
    if node is not None:
        if node.value is not None:
            codes[node.value] = prefix
        generate_huffman_codes(node.left, prefix + '0', codes)
        generate_huffman_codes(node.right, prefix + '1', codes)

def huffman_encode(binary_sequence, codes):
    encoded_sequence = ''
    i = 0
    while i < len(binary_sequence):
        for chunk, code in codes.items():
            if binary_sequence[i:].startswith(chunk):
                encoded_sequence += code
                i += len(chunk)
                break
    return encoded_sequence


binary_sequence = '10101010101'
#binary_sequence = '1111101010100001101011111'

# Find and replace chunks in the original sequence
chunks = {}
alphabet = ord('A')  # ASCII code for the first alphabet symbol
while True:
    chunk, frequency = find_repeated_chunks(binary_sequence)
    if not chunk or len(chunk) == 1:
        break
    chunks[chr(alphabet)] = frequency
    binary_sequence = binary_sequence.replace(chunk, chr(alphabet))
    alphabet += 1

# Call single binary digits by their value
for digit in '0':
    chunks[digit] = binary_sequence.count(digit)
    binary_sequence = binary_sequence.replace(digit, digit)
for digit in '1':
    chunks[digit] = binary_sequence.count(digit)
    binary_sequence = binary_sequence.replace(digit, digit)
    
print("Chunks and frequencies after replacement:", chunks)

# Build Huffman tree
root = build_huffman_tree(chunks)

# Generate Huffman codes
codes = {}
generate_huffman_codes(root, codes=codes)

# Encode the binary sequence using Huffman codes
encoded_sequence = huffman_encode(binary_sequence, codes)

print("Huffman codes:", codes)
print("Encoded sequence:", encoded_sequence)
print("Length of encoded sequence:", len(encoded_sequence))

#Shannon bound part######################################################################
def shannon_entropy(binary_sequence):
    # Count the occurrences of each bit
    counts = Counter(binary_sequence)
    
    # Calculate the probability of occurrence for each bit
    total_bits = len(binary_sequence)
    probabilities = {bit: count / total_bits for bit, count in counts.items()}
    
    # Calculate Shannon's entropy
    entropy = sum(-prob * math.log2(prob) for prob in probabilities.values())
    return entropy

# Calculate entropy
entropy = shannon_entropy(binary_sequence)
print("Shannon's entropy:", entropy)

def shannon_source_coding_bound(binary_sequence):
    entropy = shannon_entropy(binary_sequence)
    total_bits = len(binary_sequence)
    return entropy * total_bits

# Calculate Shannon's source coding bound
source_coding_bound = shannon_source_coding_bound(binary_sequence)
print("Shannon's source coding bound (total bits):", source_coding_bound)


