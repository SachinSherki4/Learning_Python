'''
Created on 19-Oct-2024

@author: LENOVO
'''

print("1. Positional Parameter")
def bio1(name, age):
    print(f"Hey my name is {name} and I am {age} year old")
bio1("Sachin", 28)
print("\n\n")


print("2. Keyword Parameter")
def bio2(name, age):
    print(f"Hey my name is {name} and I am {age} year old")
bio2(name="Sachin", age=28)
print("\n\n")


print("3. Default Parameter")
def bio3(name, age=27):
    print(f"Hey my name is {name} and I am {age} year old")
bio3(name="Sachin", age=28)
bio3("Sachin")
print("\n\n")

print("4. Variable Length")
def add(*number):
    print(f"Sum of numbers is {number}",sum(number))
add(12,2,4,5)
print("\n\n")


print("5. Lets order some food items and prepare order details")
def order_details(item_name, quantity, *toppings, **extras):
    print(f"Order : {item_name}, Quantity : {quantity}")
    if toppings :
        print(f"Toppings : {','.join(toppings)}")
    if extras: 
        for key,value in extras.items():
            print(f"{key} : {value}")

order_details("Pizza", 2, "cheese", "pepperoni", extra_cheese=True, spicy=True)
