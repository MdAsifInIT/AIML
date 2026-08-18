# F-STRING FORMATTING (Python 3.6+): usually the most readable option
# Syntax: f"Text {expression}" - expressions evaluated inside {}
# Can perform operations directly without .format() method
# Uses 'f' or 'F' prefix before string
# f-strings evaluate expressions at runtime and build a new string

a = 5
b = 10

# F-STRING: Directly embed variables/expressions in string
print(f"sum of {a} and {b} is {a+b}")  
# Output: 'sum of 5 and 10 is 15'

# Curly braces can hold expressions, not just variable names
# Examples: {a+b}, {a*b}, {a**2}, {len(string)}, function calls, etc.