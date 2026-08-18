# SUM OF FIRST N NATURAL NUMBERS: Two approaches
# Natural numbers: 1, 2, 3, 4, 5, ...
# Sum formula: S = n * (n + 1) / 2

print("\nThis program prints the sum of first n natural numbers.\n")

n = int(input("Enter the value of n: "))  # Get n from user

# METHOD 1: Using Mathematical Formula (Most efficient)
# Formula: S = n(n+1)/2
# Example: sum of first 5 = 5*6/2 = 15
sum = (n*(n+1))/2
# Note: Using / returns float; use int() or // if you want an integer result
print("sum by formula", sum)

# METHOD 2: Using For Loop (More intuitive)
# Iterate from 0 to n and add each number
sum = 0  # Initialize sum to 0 (shadows Python's built-in sum())
for i in range(n + 1):  # range(n+1) generates: 0, 1, 2, 3, ..., n
    sum += i  # Add each number to sum (sum = sum + i)
print("sum by for loop", sum)
    
