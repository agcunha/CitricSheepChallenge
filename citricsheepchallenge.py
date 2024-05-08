import hashlib

input_string = "CitricSheep"

# Convert each character to its ASCII value and multiply by the length of the string
ascii_values = [ord(char) * len(input_string) for char in input_string]

# Find the sum of all numbers in the resulting list
sum_result = sum(ascii_values)

# Generate the SHA256 hash of the sum
sum_hash = hashlib.sha256(str(sum_result).encode()).hexdigest()

# Print the hexadecimal string result
print("HexResult:", sum_hash)
