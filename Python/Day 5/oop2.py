def psnt(a = 1):
    b = (a / 200) * 100
    return b

class Student:
    subject = "Maths"
    marks = 160
    percent = psnt(marks)
    
    
stu1 = Student()

print(stu1.percent)

l = [1,2] # pythin has a class named list so we are able to create it.
print(type(l))
    