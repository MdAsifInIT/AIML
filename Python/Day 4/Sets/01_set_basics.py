# SETS: Unordered collection of unique elements
# Set elements must be immutable (e.g., numbers, strings, tuples)
# Mutable types like lists and dicts cannot be set elements

s = {1, 2, 2, 2, 2}
print(type(s))
print(len(s))
print(s)
# Duplicates are removed automatically, so only unique values remain

s.add(5)
print(s)

empty_set = set()
# {} creates a dict, so set() is the correct empty-set constructor

print(type(empty_set))

