# STRING SLICING: Extract substring using indices
# Syntax: string[start:stop:step]
# start: Initial index (inclusive), stop: Ending index (exclusive), step: Increment
# Negative indices count from the end (-1 is the last character).

word = "abrakadabra"  # String to slice (indices: 0-10)

# POSITIVE SLICING (from start)
sl1 = word[0]  # Single character at index 0 = 'a'
sl2 = word[1:4]  # Substring from index 1 to 3 (4 exclusive) = 'bra'
print(sl1 + " " + sl2)  # Output: 'a bra'

# If you omit start or stop, Python uses the beginning or end of the string

print(word[8:])  # From index 8 to end = 'bra'

# REVERSE SLICING (negative indices)
print (word[-8:-5])  # From index -8 to -5 = 'ada'
# Note: this slice walks backward from the end but still stops before -5.