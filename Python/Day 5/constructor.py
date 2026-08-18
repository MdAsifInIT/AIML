class Student:
    def __init__(self, name, cgpa): #init needs double underscore preeciding and receeding it.
        self.name = name
        self.cgpa = cgpa
        
stu1 = Student("Abhinav", 7.9)
stu2 = Student("Mona", 7.4)
stu3 = Student("Prateek", 7.0)

print (stu1.name) 
print (stu2.name) 
print (stu3.name)

print (stu1.cgpa) 
print (stu2.cgpa) 
print (stu3.cgpa) 