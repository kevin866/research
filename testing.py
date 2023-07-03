import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import BSpline

# Define the control points
control_points = np.array([[0, 0, 0],
                          [1, 0, 0],
                          [1, 1, 0],
                          [0, 1, 0],
                          [0, 0, 1],
                          [1, 0, 1],
                          [1, 1, 1],
                          [0, 1, 1],
                          [0, 0, 0]])

# Create the B-spline surface
knots = np.array([0, 0, 0, 1, 1, 1], dtype=np.float)
degree = 2
interp_surface = BSpline(knots, control_points.T, degree, axis=0)

# Generate the surface points
u = np.linspace(0, 1, 20)  # Adjusted to match the desired resolution
v = np.linspace(0, 1, 20)  # Adjusted to match the desired resolution
u_grid, v_grid = np.meshgrid(u, v)
uv = np.column_stack([u_grid.ravel(), v_grid.ravel()])
surface_points = interp_surface(uv).T

# Reshape the surface points to match the grid dimensions
surface_points = surface_points.reshape((60, 40, 3))

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(surface_points[:, :, 0],
                surface_points[:, :, 1],
                surface_points[:, :, 2],
                cmap='viridis')
ax.scatter(control_points[:, 0], control_points[:, 1], control_points[:, 2], c='r')



# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Closed-Form B-Spline Surface')

# Show the plot
plt.show()

