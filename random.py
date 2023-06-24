import random

def generate_random_binary():
    """
    Generates a random 4-digit binary number.
    
    Returns:
        str: The generated random binary number.
    """
    binary = ''.join(random.choice(['0', '1']) for _ in range(4))
    return binary

def convert_to_base_10(binary):
    """
    Converts a binary number to base 10.
    
    Args:
        binary (str): The binary number to convert.
    
    Returns:
        int: The base 10 equivalent of the binary number.
    """
    decimal = int(binary, 2)
    return decimal

# Generate a random binary number
random_binary = generate_random_binary()

# Convert the binary number to base 10
decimal = convert_to_base_10(random_binary)

print(f"Random Binary: {random_binary}")
print(f"Decimal: {decimal}")
