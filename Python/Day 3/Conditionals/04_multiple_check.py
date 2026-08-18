# MODULUS & DIVISIBILITY: Check if number is divisible
# If number % divisor == 0, then number is divisible by divisor
# Multiple of 5: 5, 10, 15, 20, 25, ... (all divisible by 5)

print("This program is to check if a number is multiple of 5.")

a = int(input("Enter a number: "))  # Get number from user
# The % operator gives the remainder after division

if a % 5 == 0:  # If remainder is 0, it's divisible by 5
    print ("Number is a multiple of 5.")
else:  # If remainder is not 0, it's not divisible by 5
    print("Number is not a multiple of 5.")