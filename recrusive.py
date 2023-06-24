def recursive_search(numbers, target, start_index=0):
    """
    Recursive searching algorithm to find a target number in a list of numbers.
    
    Args:
        numbers (list): The list of numbers to search in.
        target (int): The target number to find.
        start_index (int): The starting index for the search (default: 0).
    
    Returns:
        int: The index of the target number if found, or -1 if not found.
    """
    # Base case: If the start index exceeds the list length, the target is not found
    if start_index >= len(numbers):
        return -1

    # Base case: If the current number is the target, return its index
    if numbers[start_index] == target:
        return start_index

    # Recursive case: Search for the target in the rest of the list
    return recursive_search(numbers, target, start_index + 1)


# Example usage
numbers = [4, 2, 8, 5, 1, 6, 7, 3]
target = int(input("Enter a number to search for: "))

index = recursive_search(numbers, target)

if index != -1:
    print(f"The number {target} is found at index {index}.")
else:
    print(f"The number {target} is not found in the list.")
