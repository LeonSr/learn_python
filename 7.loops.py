#while

# v1
name = ""
while len(name) == 0:
    name = input("Enter you name: ")
print ("hello "+name)


#v2
name = None
while not name:
    name = input("Enter you name: ")
print ("hello "+name) 


# infinit loop 
while True:
    print("im okey")

#for

for i in range(10):
    print(i+1)

for i in range(50,100+1,2):
    print(i)

for i in "sina rasooli":
    print(i)