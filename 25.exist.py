import os

path = "C:\\users\\sina\\Desktop\\test.txt"

if os.path.exists(path):
    print("that location exists")
    if os.path.isfile(path):             # to verify file
        print("this is a file")
    elif os.path.isdir(path):            # to verify folder
        print("this is a directory")
else:
    print("that location doesnt exist!")