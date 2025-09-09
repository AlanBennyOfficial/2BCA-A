import time

def linear_time(n):
    print(f"\nO(n) for n = {n}")
    start = time.time()
    for i in range(n):
        pass  # Simulate some work
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")
    
linear_time(10000)
linear_time(20000)
linear_time(40000)