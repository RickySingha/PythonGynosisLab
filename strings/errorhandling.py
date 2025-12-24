string = input("Enter the string: ")

try:
    string[2] = 'C'
except TypeError as e:
    print(f"error caught {e}")
    print("Strings are immutable")