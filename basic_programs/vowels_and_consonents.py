
string=input("Enter string to check vowels and consonants in string.")

def check_vowels_and_consonants_in_string(string):
    vowels="aeiouAEIOU"
    vowel_count=sum(1 for char in string if char in vowels)
    consonant_count=len(string) - vowel_count
    print(f"In String {string} total vowels present : {vowel_count} and Consonant present : {consonant_count}")

check_vowels_and_consonants_in_string(string)

