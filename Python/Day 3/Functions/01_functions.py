# FUNCTIONS: Reusable blocks of code that perform specific tasks
# Definition (def): Creates a function
# Parameters: Variables in function definition (a, b)
# Arguments: Values passed when calling function
# Return value: Value sent back to caller

def sum(a = 1, b = 1):  # Default parameters: if not provided, use 1
    """Function definition: a and b have default values of 1"""
    c = a + b  # Add the two parameters
    print(c)  # Print the result

# Note: Naming this function "sum" shadows Python's built-in sum() function

# FUNCTION CALLS: Executing the function with different arguments
sum(5,10)  # Calls function with arguments 5 and 10 → Output: 15
sum(10,15)  # Calls function with arguments 10 and 15 → Output: 25
sum(15,20)  # Calls function with arguments 15 and 20 → Output: 35

# PARTIAL ARGUMENTS: Using default parameters
sum(6)  # Only 1 argument provided, b uses default value 1 → Output: 7
sum()  # No arguments provided, both use default values (1, 1) → Output: 2

# FUNCTION TYPES:
# - Built-in: Pre-defined functions like print(), input(), len() (provided by Python)
# - User-defined: Custom functions created by programmer (like sum() above)
