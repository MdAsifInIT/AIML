# MODULUS OPERATOR: Returns remainder after division
# Syntax: number % divisor
# Used to check divisibility: if number % 2 == 0 → even; if number % 2 == 1 → odd

print("\nThis program is to check whether a number is odd or even.\n")

num = int(input("Enter a Number: "))  # Get number from user

# Check if number is even (divisible by 2, remainder is 0)
# For non-negative integers, remainder is always 0 or 1 when dividing by 2
if num % 2 == 0:  # Even: num % 2 == 0
    print("The Number is Even.")
else:  # Odd: num % 2 == 1 (or != 0)
    print("The Number is Odd.")