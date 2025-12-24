count_dict = {}

tup = (1,4,5,2,7,8,1,2,4,5)

for n in tup:
    if n in count_dict:
        count_dict[n]+=1
    else:
        count_dict[n] = 1

print(f"Count of occurences: {count_dict}")