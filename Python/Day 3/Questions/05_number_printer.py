# POSITIVE/NEGATIVE/ZERO CLASSIFIER: Continuously classify numbers until user quits
# Logic:
# - If number > 0 → Positive (+ve)
# - If number < 0 → Negative (-ve)
# - If number == 0 → Zero
# - If input == "Quit" → Exit program

print("\nThis python program prints the sign of an integer.\nEnter \"Quit\" to exit!")

num = 0  # Initialize variable

# Infinite loop until user chooses to quit
while str(num) != "Quit":  # Continue while input is not "Quit"
    num = input("Enter a number: ")  # Get input from user (still a string)
    
    if num == "Quit":  # Check if user wants to exit
        print("\nQuiting\n")  # Print exit message
        break  # Exit loop
    
    # Check the sign of the number
    if int(num) > 0:  # Positive (int() converts the string to a number)
        print("+ve")
    elif int(num) < 0:  # Negative
        print("-ve")
    elif int(num) == 0:  # Zero
        print("0")

        