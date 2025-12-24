original_list = [1,2,3,4,5]

deep_copy  = [num for num in original_list]
shallow_copy = original_list
shallow_copy[0] = 10
deep_copy[1] = 12

print(f"Original list: {original_list}\nShallow copied list: {shallow_copy}\nDeep copied list: {deep_copy}")