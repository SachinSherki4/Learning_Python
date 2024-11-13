
print("1. Open File and reading entire file using 'r' mode and read() ")
file = open("../P1.txt", 'r')
content=file.read()
print(content)
file.close()

print("2. Reding file Line by line using readline()")
file = open("../P1.txt", 'r')
content=file.readline()
print(content)
file.close()

print("3. Reading all line using readlines() in list format")
file = open("../P1.txt", 'r')
content=file.readlines()
print(content)
file.close()