# DATA SET: Each tuple is (student_name, course_name)
info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]
# 1. List all unique course
# A set automatically keeps only unique values

set_course = set()

for i in range(len(info)):
    temp = info[i]
    set_course.add(temp[1])
    
print(set_course)

# 2. List all students enrolled in english
# We use a set to avoid duplicate student names

set_engstu = set()

for i in range(len(info)):
    temp = info[i]
    if temp[1] == "English":
        set_engstu.add(temp[0])
          
print(set_engstu)

# 3. create dictionary (Student, Set of courses)
# This builds a mapping from student -> set of courses
data = {}

for name,subject in info:
    if (data.get(name) == None):
        data.update({
            name: set()
        })
        data[name].add(subject)
        
    else:
        data[name].add(subject)
        

# Each student gets their own set, created on first encounter

print(data)


