import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the control points for the cross-shaped geometry
control_points = np.array([
    [[0.0, 0.0, 0.0], [0.5, 0.0, 0.0], [1.0, 0.0, 0.0]],  # X-axis curve
    [[1.0, 0.0, 0.0], [1.0, 0.0, 1.0], [1.0, 0.0, 2.0]],  # Z-axis curve
    [[1.0, 0.0, 2.0], [0.5, 0.0, 2.0], [0.0, 0.0, 2.0]],  # -X-axis curve
    [[0.0, 0.0, 2.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0]],  # -Z-axis curve
    [[0.0, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 1.0, 0.0]],  # Y-axis curve
    [[0.0, 1.0, 0.0], [0.0, 1.0, 1.0], [0.0, 1.0, 2.0]],  # -Y-axis curve
])

# Set up the parameter values for the Bezier curves
t = np.linspace(0, 1, 100)

# Generate the Bezier curves for each axis
x_curve = np.zeros((100, 3))
y_curve = np.zeros((100, 3))
z_curve = np.zeros((100, 3))

for i in range(3):
    x_curve[:, i] = np.polyval(control_points[0, i], t)
    y_curve[:, i] = np.polyval(control_points[4, i], t)
    z_curve[:, i] = np.polyval(control_points[1, i], t)

# Create the surface by combining the Bezier curves
surface = np.zeros((100, 100, 3))
for i in range(100):
    for j in range(100):
        surface[i, j, :] = np.polyval(x_curve[i, :], t[j]), np.polyval(y_curve[i, :], t[j]), np.polyval(z_curve[i, :], t[j])

# Extract the X, Y, and Z coordinates from the surface
x = surface[:, :, 0]
y = surface[:, :, 1]
z = surface[:, :, 2]

# Plot the surface and control points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, alpha=0.5)
ax.scatter(control_points[:, :, 0], control_points[:, :, 1], control_points[:, :, 2], c='r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
