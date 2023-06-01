students = [
    ("sina","A",20),
    ("tina","B",20),
    ("mani","C",19),
    ("parviz","D",24),
]

students.sort()

for i in students:
    print(i)

print("==========================")

grade = lambda grade:grade[1]
students.sort(key=grade)

for i in students:
    print(i)
    
print("==========================")

grade = lambda grade:grade[1]
students.sort(key=grade,reverse=True)

for i in students:
    print(i)

print("==========================")

grade = lambda grade:grade[1]
sorted_student = sorted(students,key = grade)

for i in sorted_student:
    print(i)