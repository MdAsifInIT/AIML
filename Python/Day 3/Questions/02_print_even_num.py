# PRINT EVEN NUMBERS: Function that prints even numbers in a range
# Even numbers: Divisible by 2 (remainder 0 when divided by 2)
# Logic: Check if number % 2 == 0

def evencount(a, b):
    """Print all even numbers between a and b (exclusive of b)"""
    for i in range(a, b):  # Loop from a to b-1 (b is excluded)
        if i % 2 == 0:  # Check if even (divisible by 2)
            print(i)  # Print the even number

# Example: evencount(1, 10)
# Prints: 2, 4, 6, 8
evencount(1, 10)