tuple1 = (1, 2, 3)
tuple2 = ("A", "B", "C")

print(f"Before Swap: tuple1 = {tuple1}, tuple2 = {tuple2}")

tuple1, tuple2 = tuple2, tuple1

print(f"After Swap:  tuple1 = {tuple1}, tuple2 = {tuple2}")