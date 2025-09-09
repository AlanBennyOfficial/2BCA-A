def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    steps = 0  # Count steps to illustrate log n

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            print(f"Found {target} in {steps} steps.")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print(f"{target} not found after {steps} steps.")
    return -1

# Example usage
arr = list(range(1, 6))  
binary_search(arr, 4)
