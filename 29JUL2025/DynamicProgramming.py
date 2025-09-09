def fib(n, memo={}):
    # If already computed, return stored value
    if n in memo:
        return memo[n]
    
    # Base cases
    if n <= 2:
        return 1
    
    # Recursive computation with memoization
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Example:
print("Fibonacci (DP):", fib(10))  # Output: 55