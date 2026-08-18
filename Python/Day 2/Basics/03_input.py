# INPUT HANDLING & TYPE CONVERSION
# input() function: Reads user input from console and returns it as a STRING
# int() function: Converts string to integer for mathematical operations
# If the input is not numeric, int() will raise a ValueError

x = input("Enter you name: ")  # Takes string input (returns str type)

# int() wraps input() to convert the string input directly to integer
a = int (input("Enter first number: "))  # Converts string to int
b = int (input("Enter second number: "))  # Converts string to int

# Arithmetic operation on integers
c = a + b  # Add the two numbers and store in variable c

# Display results
print("The Sum is: ", c)  # Output the sum
print("Your name is:", x)  # Output the user's name