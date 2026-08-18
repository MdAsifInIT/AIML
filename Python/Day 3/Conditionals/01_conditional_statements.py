# CONDITIONAL STATEMENTS: Execute different code based on conditions
# if: Execute block if condition is True
# elif: "else if" - Check another condition if previous was False
# else: Execute if all previous conditions are False

age = int(input("Enter your age: "))  # Get age from user

# Check if eligible to vote (age >= 18)
# Using a compound condition lets us define a valid age range in one check
if (age >= 18) and (age <120):  # Multiple conditions using AND operator
    print("Congo!", age, "years wasted, but you can vote!")

# Check if age seems impossible (>= 120)
elif (age >= 120):
    # f-strings insert variable values directly into the string
    print(f"You're dead man at {age}!\nHow're you even alive?! Damn!")

# Age is less than 18
else:
    print("Small baby, come later!\nGo have your supper, little kiddo!")