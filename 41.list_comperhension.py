print("example 1")

squares = []
for i in range(1,11):
    squares.append(i*i)
print("version 1 =>")
print(squares)

squares = [i*i for i in range(1,11)]
print("version 2 =>")
print(squares)


print("------------------------------------------")


print("example 2")

students = [100,90,80,70,60,50,40,30,0]

passed_students1 = list(filter(lambda x : x >= 60 ,students))

passed_students2 = [ i for i in students if i >= 60]

passed_students3 =  [ i if i >= 60 else "failed" for i in students]

print("vesion num1 =>")
print(passed_students1)
print("vesion num2 =>")
print(passed_students2)
print("vesion num3 =>")
print(passed_students3)

