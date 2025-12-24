my_tuple = ("Python", [10, 20, 30])

print("Original tuple:", my_tuple)
print("ID of the list inside tuple:", id(my_tuple[1]))


my_tuple[1].append(40)
my_tuple[1][0] = 99

print("Modified tuple:", my_tuple)
print("ID of the list remains the same:", id(my_tuple[1]))