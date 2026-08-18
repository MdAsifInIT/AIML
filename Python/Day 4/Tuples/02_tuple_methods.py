# TUPLES: Immutable sequences that cannot be modified after creation
# Tuples use parentheses () and are ordered collections with indexed access
# Common use cases: fixed collections, dictionary keys, function return values

tup = (1,1,2,2,3,2,4,2,9,5,2)
# Created a tuple containing: [1, 1, 2, 2, 3, 2, 4, 2, 9, 5, 2]
# Index positions:           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TUPLE METHODS:
# Tuples have only 2 built-in methods (unlike lists which have many)

# 1. index() method:
#    - Returns the INDEX (position) of the FIRST occurrence of a value
#    - Syntax: tuple.index(value)
#    - Returns: Integer index (0-based)
#    - Raises ValueError if value is not found
#    - In this case, value 2 first appears at index 2
print(tup.index(2))  # Output: 2

# 2. count() method:
#    - Returns the TOTAL NUMBER OF TIMES a value appears in the tuple
#    - Syntax: tuple.count(value)
#    - Returns: Integer count (0 if not found, no error)
#    - Counts all occurrences: 2 appears at indices 2, 3, 5, 7, 10 = 5 times
print(tup.count(2))  # Output: 5