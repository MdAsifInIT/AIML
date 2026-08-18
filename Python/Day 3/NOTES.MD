# Python Fundamentals (Part 2)

## Concepts Covered

- Conditional Statements
- Loops
- Functions

---

# Conditional Statements

Conditional statements let our program decide what to do based on conditions (i.e., true or false expressions).

## Types of Conditional Statements in Python

1. **if** – Used to test a condition. If it’s `True`, the indented block runs.
2. **elif** – (“else if”) Used when we have multiple conditions to check.
3. **else** – Runs if all above conditions are false.

> **Note:**
> We can have standalone & multiple `if` statements but `elif` & `else` can’t be used without an `if` statement preceding them.

## Example 1

```python
age = int(input("enter age: "))

if age >= 18:
    print("you can vote")
    print("you can drive")
else:
    print("you can't vote")
    print("you can't drive")
```

## Example 2 – Traffic Lights

```python
color = input("enter color: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Look")
elif color == "green":
    print("Go")
else:
    print("wrong color")
```

---

# Logical Operators in Conditions

We can check multiple conditions using logical operators:

- `and`
- `or`
- `not`

## Example 3 – Age Category

```python
age = int(input("enter age: "))

if age < 13:
    print("child")
elif (age >= 13 and age < 18):
    print("teenager")
else:
    print("adult")
```

---

# Nesting in Conditionals

Nesting means placing one block of code inside another.

## Example – Login System

```python
username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("log in successful!")
else:
    if username != "admin":
        print("wrong user name, try again.")
    else:
        print("wrong password, try again.")
```

---

# Ternary Statements (Conditional Expressions)

A compact way to write simple `if-else` statements in one line.

## Syntax

```python
value_if_true if condition else value_if_false
```

## Example

```python
age = 18
status = "Adult" if age >= 18 else "Not Adult"
print(status)
```

> Ternary statements are recommended only for simple conditions.

---

# Match-Case Statements (Python 3.10+)

An alternative to long `if-elif-else` chains.

## Syntax

```python
match variable:
    case pattern1:
        # code
    case pattern2:
        # code
    case _:
        # default case
```

- `match` → what you're comparing
- `case` → value to match
- `_` → wildcard (default)

## Example – Traffic Lights

```python
color = input("enter color: ")

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Look")
    case "green":
        print("Go")
    case _:
        print("wrong color")
```

---

# Loops

A loop lets us execute a block of code multiple times.

## Types of Loops

1. `while` loop – repeats while condition is `True`
2. `for` loop – iterates over a sequence (list, string, range, etc.)

---

# While Loop

## Syntax

```python
while condition:
    # code block
```

## Example 1 – Print 1 to 5

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

## Example 2 – Print 5 to 1

```python
i = 5
while i > 0:
    print(i)
    i -= 1
```

## Infinite Loop

If the condition always evaluates to `True`, the loop never stops.

```python
while True:
    print("Hello")
```

---

# Loop Control Statements

## break

Stops the loop immediately.

```python
i = 1
while i <= 10:
    if (i % 6 == 0):
        break
    print(i)
    i += 1
```

Output:

```
1, 2, 3, 4, 5
```

## continue

Skips the rest of the current iteration.

```python
i = 0
while (i < 10):
    i += 1
    if (i % 3 == 0):
        continue
    print(i)
```

Output:

```
1, 2, 4, 5, 7, 8, 10
```

---

# For Loop

Used to iterate over sequences.

## Syntax

```python
for variable in sequence:
    # code
```

## Example – Using range()

```python
for i in range(5):
    print(i)
```

Output:

```
0, 1, 2, 3, 4
```

---

# The range() Function

Generates a sequence of numbers.

## Parameters

1. `start` (default = 0)
2. `stop` (not included)
3. `step` (default = 1)

## Single Argument

```python
for i in range(5):
    print(i)
```

## Two Arguments

```python
for i in range(1, 6):
    print(i)
```

## Three Arguments

```python
for i in range(1, 10, 2):
    print(i)
```

---

# Looping Over Strings

```python
word = "Prime"

for ch in word:
    print(ch)
```

## Check if Character Exists

```python
if 'i' in word:
    print("letter exists")
```

## Count Occurrences

```python
word = "artificial intelligence"
count = 0

for ch in word:
    if ch == 'i':
        count += 1

print(f"i occurs {count} times.")
```

---

# Nested Loops

```python
for i in range(1, 3):
    for j in range(1, 3):
        print(f"({i}, {j})")
```

---

# Functions

Functions are reusable blocks of code that perform a specific task.

## Function Definition

```python
def hello():
    print("hello from Prime")
```

## Function Call

```python
hello()
```

---

# Functions with Parameters

```python
def sum(a, b):
    print(a + b)

print(sum(5, 10))
```

- `a, b` → parameters
- `5, 10` → arguments

## Returning Values

```python
def avg(a, b, c):
    return (a + b + c) / 3

print(avg(1, 2, 3))
```

---

# Default Parameters

```python
def sum(a, b=1):
    return a + b

print(sum(5))  # output: 6
```

> Default parameters must come last.

---

# Lambda Functions

Short, one-line anonymous functions.

## Syntax

```python
lambda arguments: expression
```

## Example – Square of a Number

```python
square = lambda x: x * x
print(square(5))
```

---

# Built-in Functions Used

- `print()`
- `input()`
- `type()`
- `range()`

---

# Practice Problems (Set 1 – Conditionals)

1. Print whether a number is multiple of 5 or not.
2. Print whether a number is odd or even.

---

# Practice Problems (Set 2 – Loops)

1. Print multiplication table of `n` (using `while`).
2. Print odd numbers from 1 to 10 using `continue`.
3. Count vowels in a word.
4. Sum of first `n` natural numbers.

---

# Practice Problems (Set 3 – Functions)

1. Create a function to compute factorial of `n`.
2. Create a function to return largest of 3 numbers (`a`, `b`, `c`).

---

# Solutions (Set 1 – Conditionals)

## 1. Multiple of 5

```python
num = int(input("enter number: "))

if num % 5 == 0:
    print("multiple of 5")
else:
    print("NOT a multiple of 5")
```

## 2. Odd or Even

```python
num = int(input("enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# Solutions (Set 2 – Loops)

## 1. Multiplication Table

```python
n = int(input("enter n: "))
i = 1

while i <= 10:
    print(i * n)
    i += 1
```

## 2. Odd Numbers (1 to 10)

```python
i = 0

while (i < 10):
    i += 1
    if (i % 2 == 0):
        continue
    print(i)
```

## 3. Count Vowels

```python
word = input("enter word: ")
count = 0

for ch in word:
    if ch in "aeiouAEIOU":
        count += 1

print("vowel count =", count)
```

## 4. Sum of First n Natural Numbers

```python
n = int(input("enter n: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("sum =", sum)
```

---

# Solutions (Set 3 – Functions)

## 1. Factorial of N

```python
n = int(input("enter n: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("factorial =", fact)
```

## 2. Largest of 3 Numbers

```python
def get_largest(a, b, c):
    if (a > b and a > c):
        return a
    elif b > c:
        return b
    else:
        return c

print(get_largest(3, 10, 5))
```

---

# Python Fundamentals (Assignment 2)

> The purpose of these questions is to build programming logic. You may take hints for mathematical parts but try to write the Python code yourself.

---

## Q1. Tax Calculator

Write a program that calculates final tax rate:

- Salary < 30,000 → 5%
- Salary 30,000–70,000 → 15%
- Salary > 70,000 → 25%

## Q2. Print Even Numbers

Write a function that takes two integers `a` and `b` and prints all even numbers between them (inclusive).

## Q3. Print Digits of a Number

Write a function that prints digits of a number `n`.

**Hint:**

- Rightmost digit → `n % 10`
- Remove rightmost digit → `n = n // 10`

## Q4. Count Digits

Write a function that returns count of digits in a number `n`.

## Q5. Sum of Digits

Write a function that returns sum of digits of number `n`.

## Q6. Divisible by 3 and 5

Print numbers from 1 to 100 divisible by both 3 and 5.

## Q7. Positive/Negative Until Quit

Continuously take input and print if number is positive or negative until user enters "Quit".

## Q8. Simple Calculator

Create:

```python
calculator(a, b, operation)
```

Where operation can be:

- `'+'`
- `'-'`
- `'*'`
- `'/'`

## Q9. Prime Number Function

Write:

```python
is_prime(n)
```

Return:

- `True` if prime
- `False` otherwise

**Hints:**

- 2 is smallest prime.
- Check divisibility in range `[2, n-1]`.

## Q10. Number Guessing Game

Create a guessing game:

- If guess > secret → "Too high"
- If guess < secret → "Too low"
- If guess == secret → "Correct!"

---

**Keep Learning & Keep Exploring!**
