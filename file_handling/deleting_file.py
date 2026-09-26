import os
if os.path.exists("greeting.txt"):
    os.remove("greeting.txt")
    print("file is deleted sucessfully!")
else:
    print("file is not found")    