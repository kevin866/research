import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import splprep, splev

def bspline_cylinder(control_points, u_resolution=5, v_resolution=2, order=3):
    u = np.linspace(0, 1, u_resolution)
    v = np.linspace(0, 2 * np.pi, v_resolution)
    U, V = np.meshgrid(v, u)
    #print(U.shape)
    n = len(control_points)
    m = len(control_points[0])

    X = np.zeros((u_resolution, v_resolution))
    Y = np.zeros((u_resolution, v_resolution))
    Z = np.zeros((u_resolution, v_resolution))

    for k in range(u_resolution):
        for l in range(v_resolution):
            for i in range(n):
              tck, _ = splprep([p[i] for p in control_points], u=np.linspace(0, 1, m), k=order)
              x, y = splev(U[k,l], tck)
              X[k, l] += x * np.cos(V[k, l])
              Y[k, l] += x * np.sin(V[k, l])
              Z[k, l] += y

    return X, Y, Z

# Define control points for the B-spline cylinder
# Define control points for the B-spline cylinder
control_points = [
    [(1, 0, 0), (1, 0, 0), (1, 0, 0)],  # Control points for the upper circle
    [(1, 0, 1), (1, 0, 1), (1, 0, 1)],  # Control points for the lower circle
]
# Generate the B-spline cylinder
X, Y, Z = bspline_cylinder(control_points, order = 2)

# Plot the B-spline cylinder
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
plt.show()