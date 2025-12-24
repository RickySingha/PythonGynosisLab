new_tuple = (1,4,5,2,7,8,110)
max_num = new_tuple[0]
min_num = new_tuple[0]

for num in new_tuple:
    max_num = max(max_num,num)
    min_num = min(min_num,num)

print(f"The maximum element is : {max_num}\nand the minimum element is : {min_num}")