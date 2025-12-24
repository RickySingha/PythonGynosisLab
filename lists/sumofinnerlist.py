nested_list = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

for index,sublist in enumerate(nested_list):
    total = sum(sublist)
    print(f"Total for list{index}: {total}")