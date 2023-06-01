import os
import shutil

path = "test.txt"

try:
    os.remove(path)         # delete a file
    #os.rmdir(path)         # delete a file or empty folder
    #shutil.rmtree(path)    # delete a folder with fils in it
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you do not have permission to delete that")
except OSError:
    print("that folder contain files")
else:
    print(path+"deletion was successful")