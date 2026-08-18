# NESTED IF-ELSE: If conditions inside other if/else blocks
# Used to handle multiple levels of decisions
# First checks outer condition, then checks nested conditions if needed

print("This program mock tests login credentials using nested if-else condition.\n")

username = input("Enter Username:")  # Get username
password = input("Enter Password:")  # Get password
# String comparisons are case-sensitive by default

# First level: Check if both username AND password are correct
if username == "admin" and password == "adminpass":  # Both must be correct
    print("Success")  # Login successful
else:
    # If first condition fails, check what was wrong
    if username != "admin":  # Check if username is wrong
        print("Wrong username")
    else:  # Username is correct but password is wrong
        print("Wrong Password")

print(":::: END OF PROGRAM ::::")  # Program complete
    

