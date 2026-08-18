# SPLITTING DECIMAL NUMBERS: Separating integer and fractional parts
# Concept: Convert number to string, then split by decimal point (.)

print ("\nWelcome to Decimal Printer \n")

a = float(input("Enter a Number: "))  # Input a decimal number (e.g., 3.14)

# Note: Converting a float to string can drop trailing zeros (3.10 -> "3.1")
# This approach is a learning-friendly way to split, not a precise formatter

# str(a) converts float to string (e.g., "3.14")
# .split('.') splits the string at decimal point into ['3', '14']
int_a, fract_a = str(a).split('.')  # Tuple unpacking: separate integer and fractional parts

# Display the two parts separately
print("\nInteger Part = ", int(int_a))  # Convert to int and display (3)
print("\nFraction Part = ", int(fract_a))  # Convert to int and display (14)