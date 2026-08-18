# TYPE CONVERSION & TYPE CASTING
# Implicit Conversion (Type Coercion): Python automatically converts types in operations
# Explicit Casting: Programmer forces conversion using conversion functions

# IMPLICIT CONVERSION: Python does it automatically
a = 5  # integer
b = 3  # integer
print(a/b)  # Output: 1.666... (Result is float because division returns float in Python 3)
print (type(a/b))  # Output: <class 'float'> - division automatically returns float

# EXPLICIT CASTING: Programmer converts types manually using conversion functions
x = 10  # integer
y = 2.5  # float
z = int((x + y))  # int() casts the result explicitly to integer (truncates, no rounding)
print(z)  # Output: 12 (int conversion removes decimal part: int(12.5) = 12)
print(type(z))  # Output: <class 'int'>

# Other Examples of Type Casting
bool_value = bool(10)  # bool() converts to Boolean
# Truthy values (converted to True): non-zero numbers, non-empty strings
# Falsy values (converted to False): 0, empty string, None
print(bool_value, type(bool_value))  # Output: True <class 'bool'>