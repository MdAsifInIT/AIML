# FUNCTION WITH PARAMETERS: Function that accepts input values
# Parameters: Variables in function definition (a, b, c, d)
# Return value: Value sent back to caller

def avg(a,b,c,d):  # Function definition with 4 parameters
    """Calculates average of 4 values"""
    x = (a + b + c + d)/4  # Sum all values and divide by count
    return x  # Return the calculated average

print("The program is to calculate your yearly performance average.")

# Get quarterly scores from user
jfm = float(input("Enter the score for JFM Quarter: "))  # Jan-Feb-Mar quarter
amj = float(input("Enter the score for AMJ Quarter: "))  # Apr-May-Jun quarter
jas = float(input("Enter the score for JAS Quarter: "))  # Jul-Aug-Sep quarter
ond = float(input("Enter the score for OND Quarter: "))  # Oct-Nov-Dec quarter

# Call function with 4 arguments and display result
# round() returns a new rounded value; it does not change the original numbers
print(round(avg(jfm, amj, jas, ond),2))  # round() limits to 2 decimal places