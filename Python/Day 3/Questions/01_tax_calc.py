# TAX CALCULATOR: Determine tax rate based on salary brackets
# Tax brackets:
# - Salary < 30,000 → 5% tax
# - Salary 30,000-70,000 → 15% tax  
# - Salary > 70,000 → 25% tax
# Formula: Tax amount = Salary × (Tax Rate / 100)

def taxcalc(salary):
    """Calculate tax amount based on salary bracket"""
    if salary < 30000:
        print("tax = 5")  # Print tax rate
        return salary * (5/100)  # Calculate 5% of salary
    
    elif (salary >= 30000) and (salary <= 70000):
        print("tax = 15")  # Print tax rate
        return salary * (15/100)  # Calculate 15% of salary
    
    else:  # salary > 70000
        print("tax = 25")  # Print tax rate
        return salary * (25/100)  # Calculate 25% of salary

print("\nThis is Salary Tax calculator.\n")

x = int(input("Enter your Salary: "))  # Get salary
y = taxcalc(x)  # Calculate tax amount (not the remaining salary)
print("The tax amount =", y)  # Display result

