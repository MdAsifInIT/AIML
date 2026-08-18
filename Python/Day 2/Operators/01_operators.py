# OPERATORS: Special symbols that perform operations on variables/values
# Three main categories: Arithmetic, Comparison, Logical, and Assignment

a = 9  # Operand 1
b = 5  # Operand 2

# ARITHMETIC OPERATORS: Used for mathematical calculations
print(a+b)  # addition: 14
print(a-b)  # subtraction: 4
print(a*b)  # multiplication: 45
print(a/b)  # division (returns float): 1.8
print(a//b)  # floor division (rounds down): 1
print(a%b)  # modulus (remainder): 4
print(a**b)  # exponentiation (a to power b): 59049

# COMPARISON OPERATORS: Return True/False by comparing values
print(a > b)  # greater than: True
print(a < b)  # less than: False
print(a >= b)  # greater than or equal: True
print(a <= b)  # less than or equal: False
print(a == b)  # equal to: False
print(a != b)  # not equal to: True

# ASSIGNMENT OPERATORS: Used to assign/modify variable values
# These lines update the same variable step by step (only the final value remains)
a = a + 2  # Traditional assignment
a += 2  # Shorthand: a = a + 2
a = a - 2
a -= 2
a = a * 2
a *= 2
a = a / 2
a /= 2
a = a // 2
a //= 2
a = a % 2
a %= 2
a = a ** 2
a **= 2

# LOGICAL OPERATORS: Combine boolean conditions
x = False
y = (5>3) and (5<4)  # AND: True only if BOTH conditions are True
print(y)  # Output: False (first condition True, second False)

z = (5>3) or (5<4)  # OR: True if AT LEAST ONE condition is True
print(z)  # Output: True (first condition is True)
