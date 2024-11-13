

print("1. Write new line by removing exisisting content in existing file using write()")
file= open("../P1.txt", 'w')
file.write("Hello, Writing single line")
file.close()

file1=open("../P1.txt", 'r')
content=file1.read()
print(content)
file1.close()
print()

print("2. Writing multiple lines by removing exisisting content in existing file using writelines()")
file2=open("../P1.txt", 'w')
lines=["First Line\n", "Second Line\n", "Third Line\n"]
file2.writelines(lines)
file2.close()

file3=open("../P1.txt", 'r')
content=file3.read()
print(content)
file3.close()