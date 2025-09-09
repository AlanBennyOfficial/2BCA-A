def find_max(arr):
    # Base case: if list has 1 element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Divide: Split the list into two halves
    mid = len(arr) // 2
    left_max = find_max(arr[:mid])  # Conquer left half
    right_max = find_max(arr[mid:]) # Conquer right half
    
    # Combine: Return the larger of the two
    return max(left_max, right_max)

# Example:
numbers = [3, 7, 2, 9, 5]
print("Max (Divide & Conquer):", find_max(numbers))  # Output: 9