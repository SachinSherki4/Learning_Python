a = 10
b = 20
print(f"Primary Value of variable a and variable b are : \na = {a} b= {b}\n")


def swapping_using_temporary_variable(no1, no2):
    a, b = no1, no2
    temp = no1
    a = b
    b = temp
    print(f"Swapping no's using temporary variable : \na = {a}\nb= {b} \n")


def swapping_using_aritmatic_operator(no1, no2):
    a = no1
    b = no2
    a = a + b
    b = a - b
    a = a - b
    print(f"Swapping using Arithmetic Operator : \na = {a}\nb= {b} \n")


def swaping_using_customize_functions(no1, no2):
    return print(f"Swapping using Customize Function : \na = {no2}\nb= {no1} \n")


def swapping_using_list(no1, no2):
    list = [no1, no2]
    list[0], list[1] = list[1], list[0]
    print(f"swapping using list : \na = {no2}\nb= {no1} \n")


swapping_using_temporary_variable(a, b)
swapping_using_aritmatic_operator(a, b)
swaping_using_customize_functions(a, b)
swapping_using_list(a, b)
