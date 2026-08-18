````markdown
# Python Fundamentals (Part 1)

## Concepts Covered

- Output / Input
- Variables
- Data Types
- Operators

---

# Output

The first and easiest thing we can do in Python is printing (outputting) something on the screen.  
We use the `print()` function to display output.

A function is a specialized helper that performs a specific task. The `print()` function helps us display information on the console.

## Syntax

```python
print("hello world")
# output will be "hello world"
```
````

Anything inside single quotes (`''`) or double quotes (`""`) is called a **string** and gets printed as it is.

### Printing Numerical Values

```python
print(3.14)
print(2 + 3)

# Output:
# 3.14
# 5
```

Each `print()` statement displays output on a new line.

To print multiple values on the same line:

```python
print("hello world", "from PRIME")
```

---

# Python Character Set

A **character set** is a collection of characters, numbers, and symbols that Python recognizes.

Common characters used in Python:

1. **English letters** – `'A' to 'Z'` and `'a' to 'z'`
2. **Digits** – `0 to 9`
3. **Special symbols** – `+ - * / % , .` etc.
4. **Whitespaces & Escape characters**
   - Blank space `" "`
   - Tab `\t`
   - Newline `\n`

5. All ASCII & Unicode characters

---

# Variables

A **variable** is like a container that stores data or values in a program.

It is a labeled box where we can:

- Store data
- Modify data
- Use data later

## Examples

```python
name = "Alex"
age = 30
PI = 3.14
word = "artificial intelligence"

print("value of PI =", PI)
```

---

## Variable Naming (Identifier) Rules

1. Must start with a letter (`a-z`, `A-Z`) or underscore (`_`)
2. Can contain letters, numbers, or underscores after the first character
3. Cannot use Python keywords like `if`, `for`, `class`, etc.

### Invalid Variable Names

```python
2name = "Bob"   # Starts with a number
class = 10      # 'class' is a keyword
```

---

## Important Notes

1. Python is **dynamically typed** (no need to declare type explicitly).
2. Python is **case-sensitive** (`age` and `Age` are different).
3. Indentation is important (standard: 4 spaces).
4. Keywords are reserved words with predefined meanings.
   - Examples: `if`, `for`, `class`, `while`, `else`, `in`, `def`

---

# Data Types

A **data type** defines the kind of value a variable can hold.

## Basic Built-in Data Types

1. `int` – Integer values (whole numbers)
2. `float` – Decimal numbers
3. `str` – Strings (sequence of characters)
4. `bool` – Boolean values (`True` / `False`)
5. `None` – Represents absence of value

Other types (covered later):

- `complex`
- `list`
- `tuple`
- `set`

---

## Checking Data Type

Use `type()` function:

```python
x = 10
print(type(x))  # <class 'int'>

PI = 3.14
print(type(PI))  # <class 'float'>

name = "Alex"
print(type(name))  # <class 'str'>

isTeacher = True
print(type(isTeacher))  # <class 'bool'>

empty_var = None
print(type(empty_var))  # <class 'NoneType'>
```

---

# Type Conversion & Type Casting

Type conversion means converting one data type into another.

## 1. Implicit Type Conversion (Automatic)

```python
a = 5
b = 3.0
print(a + b)   # Result becomes float automatically
```

## 2. Explicit Type Casting (Manual)

Common type conversion functions:

- `int()`
- `float()`
- `str()`
- `bool()`
- `list()`
- `tuple()`

Example:

```python
x = 10
y = float(x)
z = str(x)
```

---

# Operators

An **operator** is a symbol that performs operations on values (operands).

Example:

```python
print(1 + 3)   # '+' is operator, 1 and 3 are operands
```

---

## 1. Arithmetic Operators

Used for mathematical operations.

| Operator | Meaning            |
| -------- | ------------------ |
| `+`      | Addition           |
| `-`      | Subtraction        |
| `*`      | Multiplication     |
| `/`      | Division           |
| `%`      | Modulo (remainder) |
| `**`     | Power              |

Example:

```python
a = 5
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
```

---

## 2. Relational (Comparison) Operators

Used to compare values.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

Example:

```python
a = 10
b = 20

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
```

---

## 3. Assignment Operators

Used to assign values.

| Operator | Equivalent To    |
| -------- | ---------------- |
| `=`      | x = 10           |
| `+=`     | x = x + value    |
| `-=`     | x = x - value    |
| `*=`     | x = x \* value   |
| `/=`     | x = x / value    |
| `%=`     | x = x % value    |
| `**=`    | x = x \*\* value |

Example:

```python
x = 10
print("x =", x)

x += 5
print("x += 5 ->", x)

x -= 3
print("x -= 3 ->", x)

x *= 2
print("x *= 2 ->", x)

x /= 4
print("x /= 4 ->", x)

x %= 4
print("x %= 4 ->", x)

x **= 3
print("x **= 3 ->", x)
```

---

## 4. Logical Operators

Used to combine boolean values.

| Operator | Meaning                      |
| -------- | ---------------------------- |
| `and`    | True if both are True        |
| `or`     | True if at least one is True |
| `not`    | Reverses the result          |

Example:

```python
x = 10
y = 20
z = 5

print(x > z and y > x)
print(x > y or y > z)
print(not (x > y))
```

---

# Operator Precedence

Operators follow a priority order:

1. `()` – Parentheses
2. `**` – Exponent
3. `+x`, `-x`, `~x` – Unary operators
4. `*`, `/`, `//`, `%`
5. `+`, `-`
6. `<<`, `>>`
7. `&`
8. `^`
9. `|`
10. Comparison operators (`<`, `<=`, `>`, `>=`, `!=`, `==`)
11. `not`
12. `and`
13. `or`
14. Assignment operators (`=`, `+=`, `-=`, ...)

---

# Unary Operators

Unary operators work on a single operand.

Examples:

- `+x`
- `-x`
- `not`

Example:

```python
x = 5
y = -x   # unary minus

print(x)   # 5
print(y)   # -5
```

We don’t generally use `+x` because numbers are positive by default.

---

# Input

We use the `input()` function to take user input during program execution.

Whatever the user types is returned as a **string**.

## Syntax

```python
name = input("enter name: ")
print(name)
print(type(name))  # string
```

---

## Converting Input Type

Since input returns a string, we use type conversion:

```python
a = int(input("enter 1st num: "))
b = int(input("enter 2nd num: "))

print(a + b)
```

---

# Practice Problem

## Write a program that takes 2 numbers and prints their average.

```python
a = int(input("enter 1st num: "))
b = int(input("enter 2nd num: "))

avg = (a + b) / 2
print("average =", avg)
```

---

**Keep Learning & Keep Exploring!**
