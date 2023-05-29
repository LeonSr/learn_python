import os

source = "test.txt"
destination = "c:\\\user\\sina\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("there os already a file there")
    else: 
        os.replace(source,destination)
        print(source+ " was moved")
except FileNotFoundError:
    print(source+"was not found")