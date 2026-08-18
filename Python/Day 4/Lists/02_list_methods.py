# LIST METHODS: Built-in functions for lists
# Lists support many in-place updates, unlike tuples.
# Note: Most list methods modify the list in place and return None

nums = [1,2,3,4]  # Initial list

# APPEND: Add element to END of list
nums.append(5)  # List becomes: [1, 2, 3, 4, 5]

# INSERT: Add element at a specific position
nums.insert(2, 6)  # Insert 6 at index 2: [1, 2, 6, 3, 4, 5]

# SORT: Arrange elements in ascending order
nums.sort()  # Sorts in ascending order: [1, 2, 3, 4, 5, 6]
# Alternative: nums.sort(reverse=True) for descending order

# REVERSE: Reverse the order of elements
nums.reverse()  # Reverses order: [6, 5, 4, 3, 2, 1]

print(nums)  # Output: [6, 5, 4, 3, 2, 1]