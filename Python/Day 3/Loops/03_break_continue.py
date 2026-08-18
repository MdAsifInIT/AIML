# BREAK vs CONTINUE: Loop control statements
# continue: Skips current iteration and moves to next iteration
# break: Exits the loop immediately

i = 0  # Counter variable

while i < 100:  # Loop until i reaches 100
    # i + 1 is used so the printed numbers start at 1 instead of 0
    if ((i+1) % 3) == 0:  # If (i+1) is divisible by 3
        i += 1  # Increment i
        continue  # Skip to next iteration (don't print)
    else:
        print(i+1)  # Print the number
    i += 1
# Result: Prints all numbers from 1-99 EXCEPT multiples of 3 (3, 6, 9, 12, ...)