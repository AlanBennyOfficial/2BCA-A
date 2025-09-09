from array import array
my_array = array('i', [1, 2, 3, 4])
print(f"Initial Array:{my_array}")

my_array.insert(2, 25)
print(f"After Insertion:{my_array}")

my_array.remove(25)
print(f"After Removal:{my_array}")

idx = my_array.index(4)
print(f"Index of element 4 is {idx}")

my_array[3] = 99;
print(f"New array:{my_array}")

# traverse
print(f"Traversal:", end=" ")
for element in my_array:
    print(element, end=" ")
print()

