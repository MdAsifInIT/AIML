# STRING FORMATTING: Methods to insert variables into strings
# Method: .format() - using placeholder brackets {}
# format() builds and returns a new string; it does not change the originals

a = 5
b = 10
sum = a + b  # 15

# STRING FORMATTING USING format() METHOD:
# 1. Positional placeholders: {} filled in order
print("sum of {} and {} is {}".format(a, b, sum))  
# Output: 'sum of 5 and 10 is 15'

# 2. Indexed placeholders: refer to arguments by position to reorder them
print("sum of {1} and {0} is {2}".format(a, b, sum))  
# Output: 'sum of 10 and 5 is 15' (positions swapped)

# 3. Named placeholders: use names when the values are easier to read that way
print("value of a is {a} & b is {b}!" .format(a = 5, b = 10))  
# Output: 'value of a is 5 & b is 10!'