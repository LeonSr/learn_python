row = int(input("how many row?: "))
column = int(input("how many columns?: "))
symbol = input("what symbol to use?: ")

for i in range(row):
    for j in range(column):
        print(symbol , end="")
    print()