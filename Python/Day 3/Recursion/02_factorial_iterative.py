# ITERATIVE FACTORIAL: Non-recursive approach using loops
# Factorial: n! = n × (n-1) × (n-2) × ... × 2 × 1
# Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

def factorial (n):
    fact = 1  # Initialize result to 1
    
    # Multiply each number from 1 to n (inclusive)
    for i in range (1, n + 1):  # range(1, n+1) generates: 1, 2, 3, ..., n
        fact *= i  # Multiply fact by i (fact = fact * i)
    
    return fact  # Return the calculated factorial

print(factorial(4))  # Calculate and print 10! = 3,628,800