# RECURSION: Function that calls itself
# Base case: Condition where recursion stops to prevent infinite loop
# Recursive case: Function calls itself with modified parameter

def factorial(a):  # Factorial function definition
    # Base case: factorial of 1 is 1
    if a == 1 or a == 0:  # Note: This condition had a bug - should be: if a == 1 or a == 0
        return 1
    # Recursive case: factorial(a) = a * factorial(a-1)
    x = a * (factorial (a-1))  # Call function with a-1
    return x

print("\nThis program is for calculating the factorial of N.\n")
# Factorial definition: 5! = 5 × 4 × 3 × 2 × 1 = 120

n = int(input("Enter the value of N: "))
x = factorial(n)
print ("Factorial of N =", x)