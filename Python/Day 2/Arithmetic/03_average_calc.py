# AVERAGE CALCULATION: Finding the mean of two numbers
# Average Formula: (sum of all values) / (count of values)

print("Average Calculator")

a = int(input("Enter 1st Number: "))  # Get first number
b = int(input("Enter 2nd Number: "))  # Get second number

# Calculate average: (a + b) / 2
# Note: Division (/) always returns float even with integer operands
c = (a + b)/2  # Example: (5 + 7) / 2 = 6.0

# Convert result back to int, then display
# int() truncates toward zero (it does not round)
print("The average is: ", int(c))  # int(c) removes decimal part
print("Wow, you're pretty average!")