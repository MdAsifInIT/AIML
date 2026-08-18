# RANGE: Function that generates sequence of numbers
# Syntax: range(start, stop, step)
# Default values: start=0, step=1
# Note: stop value is EXCLUSIVE (not included in range)

# range(1, 100, 2) generates: 1, 3, 5, 7, ..., 99  (every 2nd number starting from 1)
# Because stop=100 is excluded, 99 is the last value

# ODD NUMBERS: All numbers not divisible by 2
# To get odd numbers from 1-99: start at 1, stop at 100, step by 2
for i in range(1, 100, 2):  # Generates: 1, 3, 5, 7, ... 99
    print(i)  # Prints each odd number