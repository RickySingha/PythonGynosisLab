original = [1,2,3,4,3,2,5,1,10]

unique = []

for num in original:
    if num not in unique:
        unique.append(num)

print(unique)