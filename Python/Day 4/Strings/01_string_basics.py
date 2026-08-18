# STRINGS: Immutable sequences of characters
# Created using quotes (' ', " ", ''' ''', """ """)
# Cannot be modified after creation (reassignment creates new string)
# Can be concatenated (combined) using +
# Can be iterated character by character

word_1 = "I love"  # First string
word_2 = "Python"  # Second string

# STRING CONCATENATION: Combining strings with + operator
sentense = word_1 + " " + word_2 + "!"  # Creates: "I love Python!"
# Concatenation builds a new string because strings are immutable
print(sentense)  # Output: I love Python!

# STRING INDEXING example kept commented out below for reference:
# print(word_2[1])  # Would output: 'y' (second character of "Python")

# ITERATION: Loop through each character in string
for ch in word_2:  # ch takes each character: 'P', 'y', 't', 'h', 'o', 'n'
    print (ch)  # Print each character on separate line