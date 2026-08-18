````markdown
# Python Fundamentals

## Assignment 3 – Solutions

---

## Q1. Check Whether a String is a Palindrome

A palindrome is a string that reads the same forward and backward.  
Examples: `"madam"`, `"racecar"`

### Program

```python
# Ask user for input
text = input("Enter a string: ")

# Reverse the string manually using a loop so the logic is visible step by step.
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

# Check palindrome
if text == reversed_text:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
```
````

---

## Q2. Compute the Average of Numbers in a List

```python
# Take list input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Calculate average; this expects at least one number.
average = sum(numbers) / len(numbers)

print("Average:", average)
```

---

## Q3. Merge Two Lists and Sort the Result

```python
# Input two lists
list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

# Merge lists into one sequence before sorting.
merged_list = list1 + list2

# Sort the merged list
merged_list.sort()

print("Sorted merged list:", merged_list)
```

---

## Q4. Separate Even and Odd Numbers from a Tuple

```python
# Input tuple
numbers = tuple(map(int, input("Enter tuple elements: ").split()))

# Split the original tuple into two new tuples based on parity.
even_tuple = tuple(num for num in numbers if num % 2 == 0)
odd_tuple = tuple(num for num in numbers if num % 2 != 0)

print("Even numbers:", even_tuple)
print("Odd numbers:", odd_tuple)
```

---

## Q5. Menu-Based Dictionary Program (Student Marks)

```python
students = {}

while True:
    # Keep showing the menu until the user exits.
    print("\nA - Add Student")
    print("B - Update Marks")
    print("C - Search Student")
    print("D - Display All")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    elif choice == 'B':
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
        else:
            print("Student not found.")

    elif choice == 'C':
        name = input("Enter student name to search: ")
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found.")

    elif choice == 'D':
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == 'E':
        break

    else:
        print("Invalid choice.")
```

---

## Q6. Create Dictionary Mapping Words to Their Length

```python
# Create a dictionary that maps each word to its length.
words = ["apple", "banana", "kiwi", "cherry", "mango"]

word_length = {word: len(word) for word in words}

print(word_length)
```

---

## Q7. Count Number of Spaces in a String

```python
text = input("Enter a string: ")

space_count = text.count(" ")  # Count literal space characters only.

print("Number of spaces:", space_count)
```

---

## Q8. Check Whether Two Lists Share No Common Elements

# Compare sets so duplicate values do not affect the disjoint check.

```python
list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

set1 = set(list1)
set2 = set(list2)

if set1.isdisjoint(set2):
    print("The lists share no common elements.")
else:
    print("The lists share common elements.")
```

---

## Q9. Print Elements That Appear More Than Once

# A simple approach that works well for small lists.

```python
numbers = list(map(int, input("Enter list elements: ").split()))

duplicates = set([num for num in numbers if numbers.count(num) > 1])

print("Elements appearing more than once:", duplicates)
```

---

## Q10. Print Unique Characters and Their Count

# A set automatically removes repeated characters.

```python
text = input("Enter a string: ")

unique_chars = set(text)

print("Unique characters:", unique_chars)
print("Count of unique characters:", len(unique_chars))
```

---

```

```
