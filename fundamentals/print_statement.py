'''
Created on 12-Oct-2024

@author: LENOVO
'''

print("1. Basic Printing")
#Syntax : print(*objects, sep=" ", end="\n", file=None, flush=False )
print("Hi My name is sachin","Yup", sep="-",end=" : ", file=None, flush=False)
print("Lets Learn Python") 
print()

print("2. Printing Multiple items")
name="Sachin"
Age=28
print("Hello my name is : ",name, " and I am ",Age," year old")

print()
print("3. Printing using customer Separator :")
print("My","name","is","Sachin",sep="-")
print()

print("4. Custom End character")
print("Hi how are you",end=", ")
print("Sachin")
print()

print("5. Formatting String literals using f-string : ")
Name="Sachin"
sub="Python"
print(f"Hi, my name is {Name} and we are going to learn {sub} from scratch")    

