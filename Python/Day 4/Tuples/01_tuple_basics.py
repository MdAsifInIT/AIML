# TUPLES: Immutable ordered collection (cannot be modified after creation)
# Created using parentheses ()
# Can contain different data types
# Indexed and sliceable like lists but unchangeable

tup = (1,2,3,4,5, "abc", 1.3)  # Tuple with mixed data types
# Data: [1, 2, 3, 4, 5, "abc", 1.3]
# Types: [int, int, int, int, int, str, float]

# SLICING: Extract portion of tuple [start:stop]
print(tup[0:3])  # Elements at indices 0, 1, 2 = (1, 2, 3)

# TYPE & LENGTH: Check type and number of elements
print(type(tup))  # Output: <class 'tuple'>
print(len(tup))  # Output: 7 (7 elements total)

# SINGLE ELEMENT TUPLE: Must use comma to distinguish from just parentheses
# (1) would be integer, but (1,) is a tuple with one element
sin_tup = (1,)
# This creates a one-item tuple, not just a grouped expression