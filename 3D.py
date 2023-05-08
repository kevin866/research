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
curve.degree_u = 1
curve.degree_v = 1
curve.degree_w = 1
curve.ctrlpts_size_u=8
curve.ctrlpts_size_v=8
curve.ctrlpts_size_w=8
# Set control points
#
curve.ctrlpts = [[float(randint(0, 100)) for _ in range(3)] for _ in range(512)]
#

print(curve.ctrlpts_size)
# Set knot vector
curve.knotvector_u = utilities.generate_knot_vector(curve.degree_u, 8)
curve.knotvector_v = utilities.generate_knot_vector(curve.degree_v, 8)
curve.knotvector_w = utilities.generate_knot_vector(curve.degree_w, 8)

# Set evaluation delta (controls the number of curve points)
curve.delta_u = 0.05
curve.delta_v = 0.05
curve.delta_w = 0.05

from matplotlib import cm

# Plot the control points grid and the evaluated surface
curve.vis = VisVTK.VisSurface()
curve.render(colormap=cm.cool)