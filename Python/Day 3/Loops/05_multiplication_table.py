# MULTIPLICATION TABLE: Prints table of a number
# Pattern: For number N, print N×1, N×2, N×3, ..., N×10

print("\nThis is a multiplication table printer.\n")

x = int(input("Enter a number: "))  # Get number

i = 0  # Counter variable

print(f"\nThe table of {x} is below:\n")  # Using f-string for formatting

while i < 10:  # Loop 10 times
    # i + 1 keeps the table from 1 to 10 instead of 0 to 9
    print(f"{x} X {i+1} = {x * (i + 1)}")  # Print: number × (i+1)
    i += 1  # Increment counter
