import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Fake mesh data
phi = np.linspace(0, np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)
phi, theta = np.meshgrid(phi, theta)
r1 = 1 + 0.1 * np.sin(5 * phi) * np.cos(3 * theta)  # Face 1
r2 = 1 + 0.2 * np.sin(5 * phi) * np.cos(3 * theta)  # Face 2 (variation)

# Convert to cartesian
x1 = r1 * np.sin(phi) * np.cos(theta)
y1 = r1 * np.sin(phi) * np.sin(theta)
z1 = r1 * np.cos(phi)

x2 = r2 * np.sin(phi) * np.cos(theta)
y2 = r2 * np.sin(phi) * np.sin(theta)
z2 = r2 * np.cos(phi)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x1, y1, z1, color='orange', alpha=0.6)
ax.plot_surface(x2, y2, z2, color='blue', alpha=0.6)

ax.axis('off')
plt.show()
