input_sequence = "0101101011101011011101101000111"

# Count occurrences of "111" in the input sequence
output_sequence = "".join(["1" if input_sequence[i:i+3] == "111" else "0" for i in range(len(input_sequence)-2)])

print("Output sequence:", output_sequence)