age = int(input("how old are u ? "))

if age <= 10:
    print("you are a child.")
elif age > 10 and age <=18:
    print("your are a teen")
elif age < 18:
    print("you are an adult")
else :
    print("the number isnt valid")

name = input(str("what is you name ? "))

if name == "sina":
    print("you are me")
elif name == "tina" or name == "mani":
    print("you are my sibling")
else:
    print("i dont know u")