# LAMBDA FUNCTIONS: Anonymous functions (functions without names)
# Syntax: lambda parameters: return_value
# Single expression only - represents the return value
# Used for short operations that might be used once
# Can be assigned to variables for later use

# Define lambda function and assign to variable 'sum'
# Note: This also shadows the built-in sum() function
sum = lambda a,b: a+b  # Lambda function that takes 2 parameters and returns their sum

# Call the lambda function using variable name
print(sum(1,2))  # Output: 3