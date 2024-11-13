
import os

print("1. Checking file exist or not before opening directly to avoid error using os module")
if os.path.exists("../P3.txt"):
    with open("../P3.txt",'r') as file :
        content=file.read()
        print(content)
else :
    print("File does not exist, Please check.\n")


print("2. Seeking file content by moving pointer to specific position using seek()")
with open("../P1.txt") as file1 :
    file1.seek(5)
    content1=file1.read()
    print(content1)
    print()


print("3. Returning pointer position using tell()")
with open("../P1.txt") as file2 :
    position=file2.tell()
    print(f"Currently POinter is present in {position} position")
