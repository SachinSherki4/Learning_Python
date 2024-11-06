'''
Created on 19-Oct-2024

@author: LENOVO
'''
import time

print("1. Calculate the sum of all no, even and odd numbers from 1 to 100 ")
print("--------------------------------------------------------------------")
Number=100
total=0
even=0
odd=0
for x in range(Number+1):
    total +=x
    if x%2==0 :
        even +=x 
    else :
        odd +=x
print(f"The sum of all even number from 1 to {Number} is {even}" )
print(f"The sum of all odd number from 1 to {Number} is {odd}" )
print(f"The sum of all number from 1 to {Number} is {total}" )
print("\n\n")


print("2. Count the number of vowels in a given string")
print("-----------------------------------------------")
String="Hello, My name is Sachin. Lets Learn Python together"
vow=[]
count=0
for char in String :
    if char.lower() in "aeiou":
        count +=1
        if  char not in vow :
            vow.append(char)
print("String : ",String)
print(f"Total {count} vowels are present in given String")
print(f"Following {vow} are present in given String")
print("\n\n")


print("3. Generate a list of prime numbers up to a specified number")
print("-------------------------------------------------------------")
no=100
prime=[]
for x in range(2,no+1):
    is_prime=True
    for i in range(2, int(x** 0.5)+1) :
        if x%i==0 :
            is_prime=False 
    if is_prime :
        prime.append(x)
print(f"Following are the prime number present in {no} : {prime}")
print("\n\n")


print("4. Calculate the factorial of a given number")
print("---------------------------------------------")
no=10
fact=1
for x in range(1,no+1):
    print(f"{fact}",end="")
    fact *= x
    print(f"*{x} = {fact}")
print(f"Factorial of {no} is {fact}")
print("\n\n")


print("5. Reverse a given string using a loop")
print("---------------------------------------------")
String="Interesting"
reverse_string=""
for char in String:
    reverse_string = char + reverse_string
print(reverse_string)
print("\n\n")


print("6. Count the frequency of each element in a list")
print("---------------------------------------------")
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}
for element in elements:
    frequency[element] = frequency.get(element, 0) + 1
print("Elements : ",elements)
print("Frequency of elements:", frequency)
print("\n\n")


print("7. Print the multiplication table for a given number")
print("---------------------------------------------")
n=9
for x in range(1,11):
    print(f"{x}*{n} = {x*n}")
print("\n\n")


print("8. Determine the largest and smallest number in a list.")
print("---------------------------------------------")
numbers = [3, 5, 1, 8, 2]
largest=numbers[0]
smallest=numbers[0]
for x in numbers:
    if x > largest :
        largest=x
    if x < smallest :
        smallest=x
print(f"List : {numbers}")
print(f"Largest no from given list is {largest}")
print(f"Smallest no from given list is {smallest}")
print("\n\n")


print("9. Create a simple countdown timer")
print("---------------------------------------------")
n=5

for x in range(n,0,-1):
    print(x)
    time.sleep(1)
print("Times Up!")