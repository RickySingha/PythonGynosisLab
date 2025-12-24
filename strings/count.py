count_vowels=0
count_consonants=0
count_digits=0
count_special_char=0

string  = input("Enter the string: ")
string = string.lower()
print(string)

for s in string:
    if s.isalpha():
        if s in 'aeiou':
            count_vowels+=1
        else:
            count_consonants+=1
    elif s.isdigit():
        count_digits+=1
    elif not s.isspace():
        count_special_char+=1

print(f"Total count of vowels: {count_vowels}\nTotal count of consonants = {count_consonants}\nTotal count of digits: {count_digits}\nTotal count of special characters: {count_special_char}")
