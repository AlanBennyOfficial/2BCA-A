import matplotlib.pyplot as plt
import math

n_values = list(range(1, 11))
linear = [n for n in n_values]
quadratic = [n**2 for n in n_values]
exponential = [2**n for n in n_values]

plt.plot(n_values, linear, label="O(n)")
plt.plot(n_values, quadratic, label="O(n²)")
plt.plot(n_values, exponential, label="O(2ⁿ)")
plt.xlabel("Input size (n)")
plt.ylabel("Operations")
plt.title("Growth Rate Comparison")
plt.legend()
plt.grid(True)
plt.show()
