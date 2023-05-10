from geomdl import BSpline
import tools
from geomdl import BSpline
from geomdl import CPGen
from geomdl import utilities
from geomdl import construct
from geomdl import operations
from geomdl.visualization import VisVTK
from random import randint

# Create a 3-dimensional B-spline Curve
curve = BSpline.Volume()

# Set degree
curve.degree_u = 2
curve.degree_v = 2
curve.degree_w = 2
curve.ctrlpts_size_u=3
curve.ctrlpts_size_v=3
curve.ctrlpts_size_w=3
# Set control points
#
curve.ctrlpts = tools.random_digits(3,6,6)
#tools.random_digits(3,6,6)
#
#curve.ctrlpts = [[float(randint(0, 10)) for _ in range(3)] for _ in range(512)]

#print(curve.ctrlpts)
# Set knot vector
curve.knotvector_u = utilities.generate_knot_vector(curve.degree_u, 3)
curve.knotvector_v = utilities.generate_knot_vector(curve.degree_v, 3)
curve.knotvector_w = utilities.generate_knot_vector(curve.degree_w, 3)
#print(curve.knotvector_w)
# Set evaluation delta (controls the number of curve points)
curve.delta_u = 0.05
curve.delta_v = 0.05
curve.delta_w = 0.05

from matplotlib import cm

# Plot the control points grid and the evaluated surface
curve.vis = VisVTK.VisSurface()
curve.render(colormap=cm.cool, animate=True)