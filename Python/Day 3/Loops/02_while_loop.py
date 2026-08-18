# WHILE LOOPS: Repeat a block of code as long as a condition is True
# Iterator: Variable that changes on each iteration
# Syntax: while condition:
# Note: Must update iterator to avoid infinite loops
# If x never changes, the condition stays True forever

x = 0  # ITERATOR: Starts at 0

while x < 10:  # Loop continues while x is less than 10
    print("Hello World!")  # Print statement
    x += 1  # Increment x by 1 on each iteration (x = x + 1)
# After loop: x = 10, condition (10 < 10) is False, so loop stops