def generate_combinations(n, s):
    # Base case
    if n == 1:
        return list(s)

    result = []
    for ch in s:
        # Recursively generate (n-1)-length combinations
        for tail in generate_combinations(n - 1, s):
            result.append(ch + tail)
    return result

# Example usage
combinations = generate_combinations(3, 'abc')
print(combinations)
