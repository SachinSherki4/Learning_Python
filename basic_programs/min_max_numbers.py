
numbers =input("Enter three number with space like 1 4 6 8 : ").split(" ")

def find_min_max_numbers_using_loop(numbers):
    numbers =numbers
    number =[int(x) for x in numbers]
    max_no =number[0]
    min_no =number[0]
    for no in number :
        if max_no < no :
            max_no =no
        if min_no > no :
            min_no =no
    print(f"Minimun Number is : {min_no} and Maximum Number is : {max_no}")

def find_min_max_numbers_using_sorted_functions(numbers):
    number =[int(x) for x in numbers]
    sorted_no =sorted(number)
    print(f"Minimun Number is : {sorted_no[0]} and Maximum Number is : {sorted_no[-1]}")



find_min_max_numbers_using_loop(numbers)
find_min_max_numbers_using_sorted_functions(numbers)
