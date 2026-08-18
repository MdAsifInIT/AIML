# EXTRACT DIGITS: Function that prints each digit of a number separately
# Algorithm:
# 1. Get rightmost digit: number % 10
# 2. Remove rightmost digit: number = number // 10
# 3. Repeat until number becomes 0
# Example: 123 → 3, 12 → 2, 1 → 1 (prints in reverse: 3, 2, 1)

def digiprint(n):
    """Print digits of number from right to left"""
    if n == 0:  # Base case: if number is 0
        print(n)  # Print 0
        return  # Exit function
    
    # Extract and print each digit
    # This prints digits in reverse order because we peel from the right
    while n > 0:
        digit = n % 10  # Get rightmost digit (5 from 125)
        print(digit)  # Print that digit
        n = n // 10  # Remove rightmost digit (125 becomes 12)
        # Loop continues: 12 % 10 = 2, then 1
    
value = int(input("Enter a number: "))  # Get number from user
print("\n")  # Print blank line
digiprint(value)  # Print digits separately