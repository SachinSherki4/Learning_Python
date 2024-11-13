
print("Existing Data in file")
with open("../P1.txt",'r') as f:
    content=f.read()
    print(content)

print("1. Appending new lines in existing file without truncating existing data")
with open("../P1.txt",'a') as f1:
    f1.write("This is new line")

with open("../P1.txt",'r') as f4 :
    content6=f4.read()
    print(content6)

print("2. Appending new file with existing file")
with open("../P1.txt",'a') as f2 :
    with open("../P2.txt",'r') as f3 :
        contentt=f3.read()
        f2.write("\n")
        f2.write(contentt)
        

with open("../P1.txt",'r') as f4 :
    content6=f4.read()
    print(content6)
    