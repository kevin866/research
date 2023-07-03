import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the radius and height of the cylindrical cross
radius = 1.0
height = 2.0

# Define the number of control points in each direction
num_points = 5

# Generate control points for the x-direction
x_control_points = np.zeros((num_points, 3))
x_control_points[:, 0] = np.linspace(-radius, radius, num_points)

# Generate control points for the y-direction
y_control_points = np.zeros((num_points, 3))
y_control_points[:, 1] = np.linspace(-radius, radius, num_points)

# Generate control points for the z-direction
z_control_points = np.zeros((num_points, 3))
z_control_points[:, 2] = np.linspace(0, height, num_points)

# Combine the control points in all three directions
control_points = np.concatenate((x_control_points, y_control_points, z_control_points), axis=0)
print(control_points)

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the control points
ax.scatter(control_points[:, 0], control_points[:, 1], control_points[:, 2], c='red', marker='o')

# Set plot limits and labels
ax.set_xlim(-radius, radius)
ax.set_ylim(-radius, radius)
ax.set_zlim(0, height)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()