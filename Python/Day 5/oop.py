# Class is basically a blueprint of the object. They do not take up space in memory
# object is an instance of class. They take up space in memory

class Student:
    subject = "Python"
    college = "ABC"
    year = "4th Year"
    
    
stu1 = Student()
stu2 = Student()

# The data can be accessed using a dot operator
print(stu1.subject) 
print(stu1.college)
print(stu1.year)

print("\n")

print(stu2.subject) 
print(stu2.college)
print(stu2.year)

# This student can be stored in a list for better usability.