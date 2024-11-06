'''
Created on Aug 3, 2024

@author: ssherki
'''
from datetime import datetime

a="My name is Sachin N Sherki "
print(a.strip(a))
print(a.find("name"))
print(a.find("N"))
print(a.index("name"))
d=a.split()

for x in d:
    print(x)
print('-'.join(a)) #M-y- -n-a-m-e- -i-s- -S-a-c-h-i-n- -N- -S-h-e-r-k-i- 
print('-'.join(d)) # My-name-is-Sachin-N-Sherki
print(':'.join(d)) # My:name:is:Sachin:N:Sherki

print("Reversing the String ")
print()
print("Using slice operator : ",a[::-1])
print("Using seperator operator : ", "".join(reversed(a)))

b=""
l=len(d)-1
while(l>=0):
    for x in d[l] :
        b=b+x 
    l=l-1
    b=b+' '
print(b)    


print()
print("Formating Decimal ")

print("Formating Integer No which is {}".format(123))
print("Formating Integer No which is {:d}".format(123))
print("Formating Integer No which is {:5d}".format(123))
print("Formating Integer No which is {:05d}".format(123))


print("Formating Floating numbers ")

print("Formating Floating No which is {}".format(123))
print("Formating Floating No which is {:f}".format(123))
print("Formating Floating No which is {:f}".format(123.45687))
print("Formating Floating No which is {:8.3f}".format(123.456798))
print("Formating Floating No which is {:08.3f}".format(123.34))
print("Formating Floating No which is {:08.3f}".format(9876123.98765))

print()
# Truncating String using Format() method
print("1 Truncating String using Format() method ")

Max_Lenth=10
Text = "Hello My name is Sachin"
Truncate_Text="{:.{width}}".format(Text,width=Max_Lenth)
print(Truncate_Text)



print()
print("2 Formating Dictionary Members using Format ")
person={"Name": "Sachin", "Age":28, "Location": "Pune", "Salary" : 150000}
person1={"Details": {"Name": "Sachin", "Age":28, "Location": "Pune"}, "Salary" : 150000}
print("Hello, My name is {Name} and age {Age} currently working in {Location} having salary of RS {Salary}/month".format(**person))
print("Hello, My name is {Details[Name]} and age {Details[Age]} currently working in {Details[Location]} having salary of RS {Salary}/month".format(**person1))


print()
print("3. Formating String using F-String ")
Name ="Sachin" 
Age = 28 
Location = "Pune"
Salary = 150000

formatted_details= f"Hello! My name is : {Name} age :{Age} currently in {Location} having salary of RS {Salary}/month"
print(formatted_details)


print()
print("4. Calculation inside f-strin")
a=23
b=98
c=56.3454
d=23.45
print(f"Addition of {a} and {b} = {a+b}")
print(f"Multiplication of {a} and {c} with only 2 decimal = {a * c:.2f}")


print()
print("5. Formating Dictionary members using f-string")

person={"Name": "Sachin", "Age":28, "Location": "Pune", "Salary" : 150000}
person1={"Details": {"Name": "Sachin", "Age":28, "Location": "Pune"}, "Salary" : 150000}

print(f"Hello, My name is {person['Name']} and age {person['Age']} currently working in {person['Location']} having salary of RS {person['Salary']}/month")
print(f"Hello, My name is {person1['Details']['Name']} and age {person1['Details']['Age']} currently working in {person1['Details']['Location']} having salary of RS {person1['Salary']}/month")


print()
print("6. f-sting for conditional expression")

a=67
b=54
print(f"Grater no between {a} and {b} is {a if a >=b else b}")


print()
print("7. Formating date and time")

curentdate =datetime.now()
formatted_Date_Time= f"Today's date and time is : {curentdate:%y-%m-%d %H:%M:%S}"
print(formatted_Date_Time)

print()
print("8. Functions call and Expression in f-string")

def great(name):
    return f"Hello!, {name}"
name = "sachin"
formatted_string= f"{great(name)} welcome to the world of Python"
print(formatted_string)







