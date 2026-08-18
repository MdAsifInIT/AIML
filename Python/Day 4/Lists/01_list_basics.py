# LISTS: Mutable (changeable) ordered collection of items
# Created using square brackets []
# Indexed: Access elements by position (0-based indexing)
# Can contain different data types
# Key difference from tuples: lists can be modified after creation

marks = [99, 98, 100, 65, 92]  # List of 5 marks
print(marks)  # Output: [99, 98, 100, 65, 92]

# INDEXING: Access individual element by position
print(marks[0])  # First element (index 0) = 99
print(f"the index value of last element is {len(marks) - 1}")  # Last index = len(marks) - 1 = 4

# TYPE: Check data type
print(type(marks))  # Output: <class 'list'>

# SLICING: Extract portion of list [start:stop]
# start: inclusive, stop: exclusive
print(marks[0:2])  # Elements at indices 0, 1 = [99, 98]
print(marks[3:len(marks)])  # Elements from index 3 to end = [65, 92]

# Negative indices count from the end: -1 is the last element