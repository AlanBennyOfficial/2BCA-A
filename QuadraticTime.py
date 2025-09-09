import time

def quadratic_time(n):
    print(f"\nO(n²) for n = {n}")
    start = time.time()
    for i in range(n):
        for j in range(n):
            pass  # Simulate some work
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")

quadratic_time(200)
quadratic_time(400)
quadratic_time(800)
