
print("1. Reading existing content in file")

with open("../P1.txt",'r') as f:
    existing_content=f.read()
    print(existing_content)
    
print("\n2. Now read and write at same time using r+ mode")

with open("../P1.txt",'r+') as f1:
    content=f1.read()
    print(f1.tell())
    f1.write("This is Updating line adding at the end of file.\n")
    f1.write("File Update successfully.\n")
    updated_content=f1.read()
    print(updated_content)