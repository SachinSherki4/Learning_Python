import string

user_enter_string = input("Enter any line which involve some special chanracters : ")


def remove_string_punchuation(user_string):
    clean_text = ''.join(char for char in user_string if char not in string.punctuation)
    print(f"Old String : {user_string}")
    print(f"Updated String : {clean_text}")


def remove_particular_special_char_from_string(user_string):
    punctuation = "!"
    clean_text = ''.join(char for char in user_string if char not in punctuation)
    print(f"Old String : {user_string}")
    print(f"Updated String : {clean_text}")


remove_string_punchuation(user_enter_string)
remove_particular_special_char_from_string(user_enter_string)