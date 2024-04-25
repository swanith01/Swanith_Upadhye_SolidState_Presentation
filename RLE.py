from collections import Counter
import math

#RLE Compressor function
def rle_compress(binary_sequence):
    compressed_sequence = ''
    count = 1
    for i in range(1, len(binary_sequence)):
        if binary_sequence[i] == binary_sequence[i - 1]:
            count += 1
        else:
            compressed_sequence += str(count) + 'x' + binary_sequence[i - 1] + ', '
            count = 1
    compressed_sequence += str(count) + 'x' + binary_sequence[-1]
    return compressed_sequence

#Examples:
#binary_sequence = '000011110000'
#binary_sequence= '0000000111111111111111111111111111111111111110000000000111111'
binary_sequence='0011100'

compressed_sequence = rle_compress(binary_sequence)
print("Compressed Sequence:", compressed_sequence)
print("Length of compressed sequence:", len(compressed_sequence))

# Source coding Bound
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

def average_run_length(binary_sequence):
    count = 1
    total_runs = 1
    for i in range(1, len(binary_sequence)):
        if binary_sequence[i] == binary_sequence[i - 1]:
            count += 1
        else:
            total_runs += 1
            count = 1
    return len(binary_sequence) / total_runs

# Calculate adjusted Shannon bound
def adjusted_shannon_bound(binary_sequence):
    entropy = shannon_entropy(binary_sequence)
    avg_run_length = average_run_length(rle_compress(binary_sequence))
    return entropy * avg_run_length

# Example usage
adjusted_bound = adjusted_shannon_bound(binary_sequence)
print("Adjusted Shannon bound (total bits):", adjusted_bound*len(compressed_sequence))


