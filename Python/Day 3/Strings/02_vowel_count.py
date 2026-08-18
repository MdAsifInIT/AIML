# NESTED LOOPS: Loop inside another loop
# Outer loop: Iterates through each character in word
# Inner loop: Checks if that character is a vowel
# Vowels: a, e, i, o, u

print("\nThis Python Program Counts Vowels in a String.\n")

word = "elephant"  # String to check
vowel = "aeiou"  # String containing all vowels
# This checks only lowercase vowels; uppercase vowels would need extra handling
j = 0  # Counter for vowel count

# Outer loop: iterate through each character in word
for var in word:  # var = 'e', 'l', 'e', 'p', 'h', 'a', 'n', 't' (each character)
    # Inner loop: check if current character matches any vowel
    for var1 in vowel:  # var1 = 'a', 'e', 'i', 'o', 'u' (each vowel)
        if var == var1:  # If character is a vowel
            j += 1  # Increment vowel counter

# Result: 'e' appears 2 times, 'a' appears 1 time = 3 vowels total
print (j)