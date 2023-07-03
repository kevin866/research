import numpy as np

import pyvista as pv
from pyvista import examples
rng = np.random.default_rng()
points = rng.random((5,5,5, 3))
points
pv.plot(points)
