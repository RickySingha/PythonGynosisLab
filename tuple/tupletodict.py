list_of_tuples = [(1,2,3,4,5),(6,7,8,9,10)]

todict = {}
i = 1
for tup in list_of_tuples:
    todict[f"tup{i}"] = tup
    i+=1

print(todict)