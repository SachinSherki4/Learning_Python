
name="Hi! my name is Sachin Sherki"
print(f"Original String : {name}\n")

def reversing_characters_using_loop(string):
    revers_name=""
    for char in string :
        revers_name=char+revers_name
    print(f"Reversing all character though Loops : {revers_name}")

def reversing_characters_using_slicing_operator(string):
    slicing=string[: :-1]
    print(f"Reversing all charactor using slicing : {slicing}")

def reversing_sequence_of_words(string):
    reverse=""
    for l in string.split(" "):
        reverse=l +" "+ reverse
    print(f"Reversing Sequence of words : {reverse}")

def reversing_char_in_each_words(string):
    list=string.split(" ")
    reverse=""
    for word in list:
        reverse=reverse+word[::-1]+" "
    print(f"Reversing char in each words : {reverse}")


reversing_characters_using_loop(name)
reversing_characters_using_slicing_operator(name)
reversing_sequence_of_words(name)
reversing_char_in_each_words(name)
