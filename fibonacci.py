def fibonacci_sum(n):
    """
    Calculates the sum of the first n Fibonacci numbers.
    
    Args:
        n (int): The number of Fibonacci numbers to sum.
    
    Returns:
        int: The sum of the first n Fibonacci numbers.
    """
    fib_sum = 0
    a, b = 0, 1
    count = 0
    
    while count < n:
        fib_sum += a
        a, b = b, a + b
        count += 1
    
    return fib_sum

# Calculate the sum of the first 50 Fibonacci numbers
fibonacci_sum_50 = fibonacci_sum(50)

print(f"Sum of the first 50 Fibonacci numbers: {fibonacci_sum_50}")
