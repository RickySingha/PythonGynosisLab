
def ispalindrome(string):
    string = string.lower().replace(" ","")
    length = len(string)

    for i in range(length//2):
        left_char = string[i]
        right_char=string[-i-1]

        if left_char!=right_char:
            return False
    return True

if __name__ == "__main__":
    string = input("Enter the string: ")
    if ispalindrome(string):
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")
