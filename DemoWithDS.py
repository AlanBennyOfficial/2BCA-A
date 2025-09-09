# With data structure
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 78}
]


# Finding highest
topper = max(students, key = lambda s:s["marks"])
print(f"Topper: {topper['name']} with {topper['marks']} marks")