frequency = {}
string = input("Enter the string: ")
for s in string:
    if s in frequency:
        frequency[s] +=1
    else:
        frequency[s] = 1

print(frequency)