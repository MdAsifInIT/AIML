# STRING SEARCHING: Count occurrences of a character in a string
# Loop through each character and check if it matches target character
# Using simple loop and counter variable

print("This Python program counts number of specific letters in a string.")

word = "artificial intelligence"  # String to search
# Comparisons are case-sensitive ('I' would not match 'i')

j = 0  # Counter variable to track occurrences

# Loop through each character in the word
for var in word:  # var takes each character: 'a', 'r', 't', 'i', 'f', ...
    if var == 'i':  # Check if current character is 'i'
        j += 1  # Increment counter

# Result: count how many times 'i' appears in "artificial intelligence"
print(j)  # Output: 5 (count of letter 'i')