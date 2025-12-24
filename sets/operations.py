set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

union_set = set_a | set_b 

intersection_set = set_a & set_b

difference_set = set_a - set_b


sym_diff_set = set_a ^ set_b


print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print("-" * 30)
print(f"Union:                {union_set}")
print(f"Intersection:         {intersection_set}")
print(f"Difference (A-B):     {difference_set}")
print(f"Symmetric Difference: {sym_diff_set}")