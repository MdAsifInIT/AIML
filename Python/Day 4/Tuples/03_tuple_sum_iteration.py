# TUPLE ITERATION & ACCUMULATION: Sum all values in a tuple
# Loop through each element and add to running sum
# Similar to summing numbers in a list

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # Tuple containing numbers 1-9

sum = 0  # Initialize accumulator to 0 (shadows Python's built-in sum())

# Accumulate the running total one element at a time.
for val in tup:  # val = 1, 2, 3, ... 9 (each element)
    sum += val  # Add current value to sum (sum = sum + val)

# Result: 1+2+3+4+5+6+7+8+9 = 45
print (sum)  # Output: 45
