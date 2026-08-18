# LINEAR SEARCH: Find position of element in list
# Algorithm: Compare each element with target until found or list ends
# Uses break to exit loop early once element is found

marks = [1, 2, 3, 10, 4]  # List to search

i = 0  # Index counter
x = 10  # Target value to find

# Loop through each element while tracking the position separately.
for mark in marks:  # mark = 1, 2, 3, 10, 4 (each element)
    if mark == x:  # Check if current element matches target
        print (f"x is found at index {i}")  # Found! Print position
        break  # Exit loop (don't continue searching)
    else:
        i += 1  # If not found, increment index counter

    # If x is not in the list, the loop ends without a "found" message