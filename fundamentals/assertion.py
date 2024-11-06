'''
Created on 06-Nov-2024

@author: LENOVO
'''
print("1. Ensure that user input is within an expected range ")
print("---------------------------------------------------------")
def age_set(age):
    assert age >=0, "Age cannot be Negative"
    print("Age set to : ",age)
age_set(20)
print("\n\n")


print("2. Check that a function returns the expected result")
print("------------------------------------------------------")
def add(a,b):
    return a+b

a,b=[int(x) for x in input("Enter two no seperated by space : ").split()]
result=add(a,b)
print(f" Addition of {a} & {b} is {result}")
assert result==a+b, f"Expected addition of {a} & {b} is equal to {a+b}"
print("\n\n")


print("3. Verify that a list contains only positive number")
print("----------------------------------------------------")
def postive_number(numbers):
    for x in numbers :
        assert x >0, f"Found Non-Positive number : {x}"
    print(f"{numbers} contain all positive numbers")   

l=[int(x) for x in input("Enter number separated by comma(,) : ").split(",")]
postive_number(l)
print("\n\n")


print("4. Check that an algorithm produces valid results")

def factorial(number):
    assert number >0, "Factorial is not defined for negative numbers"
    if number ==0 :
        return 1
    result =1
    for x in range(1,number+1):
        result *= x 
    return result 
print(factorial(int(input("Enter the number of which you want to count factorial : "))))