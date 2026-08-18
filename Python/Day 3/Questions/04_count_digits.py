# COUNT DIGITS: Function that counts total digits in a number
# Approach: Convert number to string, then get length
# Length of string = number of digits
# Example: 822101 → "822101" has length 6 → 6 digits
# Note: Negative numbers would include '-' in the string unless handled

def digicount(a):
    """Return count of digits in number a"""
    b = str(a)  # Convert number to string (e.g., 822101 → "822101")
    return len(b)  # Return length of string (number of characters = number of digits)

x = digicount(822101)  # Count digits in 822101
print(x)  # Output: 6 (because 822101 has 6 digits)
