"""
OPERATOR PRECEDENCE IN PYTHON
==============================

Operator precedence determines which calculations are performed first in an expression.
Higher precedence operators are evaluated before lower precedence ones.

PRECEDENCE ORDER (Highest to Lowest):
====================================

1. Parentheses ()
   - Highest precedence, forces evaluation of grouped expressions
   - Example: (2 + 3) * 4 = 20 (not 14)

2. Exponentiation **
   - Power/exponentiation operator
   - Right-to-left associativity
   - Example: 2 ** 3 ** 2 = 2 ** 9 = 512 (not 64)

3. Unary +, -, ~
   - Positive, negative, bitwise NOT
   - Example: -2 ** 2 = -4 (exponentiation first, then negation)

4. Multiplication *, Division /, Floor Division //, Modulus %
   - Left-to-right associativity
   - All have same precedence
   - Example: 10 / 2 * 3 = 15 (left-to-right)

5. Addition +, Subtraction -
   - Left-to-right associativity
   - Example: 5 + 3 - 2 = 6

6. Bitwise Shifts <<, >>
   - Left and right shift operators
   - Example: 5 << 1 = 10

7. Bitwise AND &
   - Example: 5 & 3 = 1

8. Bitwise XOR ^
   - Example: 5 ^ 3 = 6

9. Bitwise OR |
   - Example: 5 | 3 = 7

10. Comparison ==, !=, <, <=, >, >=, is, is not, in, not in
    - Equal precedence, left-to-right
    - Example: 5 > 3 > 1 = True (chained comparison)

11. Boolean NOT (not)
    - Logical NOT operator

12. Boolean AND (and)
    - Logical AND operator
    - Left-to-right associativity

13. Boolean OR (or)
    - Logical OR operator
    - Lowest precedence
    - Left-to-right associativity

EXAMPLES:
=========

Example 1: Mixed arithmetic
>>> 2 + 3 * 4
14  # Multiplication before addition

Example 2: Exponentiation and negation
>>> -2 ** 2
-4  # Exponentiation evaluated first, then negation

Example 3: Comparison chaining
>>> 5 > 3 > 1
True  # Evaluated as (5 > 3) and (3 > 1)

Example 4: Using parentheses
>>> (2 + 3) * 4
20  # Parentheses force addition first

Example 5: Boolean operators
>>> True or False and False
True  # AND has higher precedence than OR

Example 6: Complex expression
>>> 10 + 5 * 2 - 3 ** 2 / 3
>>> = 10 + 10 - 9 / 3
>>> = 10 + 10 - 3
>>> = 17

KEY POINTS:
===========
- Use parentheses to make complex expressions clearer
- Exponentiation is right-to-left associative, others are left-to-right
- Boolean operators have lowest precedence
- When in doubt, use parentheses!
"""
