set_1 = {1,2,3,4,10,8}
set_2 = {8,9,12,3,2}


common = set_1 & set_2  

print(f"Set 1: {set_1}") 
print(f"Set 2: {set_2}") 

set_1.difference_update(common)
set_2.difference_update(common)

print(f"Set 1 cleaned: {set_1}") 
print(f"Set 2 cleaned: {set_2}") 