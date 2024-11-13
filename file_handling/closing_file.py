
print("1. Closing file manually with close() function")
file=open("../P1.txt",'r')
content=file.read()
print(content)
file.close()
print()

print("2. Closing open file automatically using context manager with statement ")
with open("../P1.txt",'r') as file1:
    content1=file1.read()
    print(content1)
    