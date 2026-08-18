# MATCH-CASE STATEMENT (Python 3.10+): Structural pattern matching
# Similar to switch-case in other languages
# Syntax: match variable:
#           case value1:
#           case value2:
#           case _:  # Default case (underscore = wildcard)

print("Traffic Light Signal")

tl = input("Enter Traffic light color: ")  # Get color from user
# match-case is case-sensitive ("Green" is different from "green")

# Check the value of tl and execute corresponding block
match tl:
    case "Green":  # If tl == "Green"
        print("Go!")
    
    case "Red":  # If tl == "Red"
        print("Stop!")
    
    case "Yellow":  # If tl == "Yellow"
        print("Look!")
    
    case _:  # Default case: matches anything not matched above
        print("Wrong Color!")