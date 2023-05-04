from random import randint
from geomdl import BSpline
from geomdl.visualization import VisVTK
from geomdl import utilities
def random_digits(x, y, z):
    return [[[float(randint(0, 100)) for k in range(x)] for j in range(y)] for i in range(z)]


def generate_surface(ctrlpts, degree_u, degree_v):
    # Create a BSpline surface
    surf = BSpline.Surface()

    # Set degrees
    surf.degree_u = degree_u
    surf.degree_v = degree_v

    # Set control points
    surf.ctrlpts2d = ctrlpts

    # Set knot vectors
    surf.knotvector_u = utilities.generate_knot_vector(degree_u, len(ctrlpts))
    surf.knotvector_v = utilities.generate_knot_vector(degree_v, len(ctrlpts[0]))
    #surf.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0,4.0]
    #surf.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0,4.0]

    # Set evaluation delta
    surf.delta = 0.025

    # Evaluate surface points
    surf.evaluate()

    # Import and use Matplotlib's colormaps
    from matplotlib import cm

    # Plot the control points grid and the evaluated surface
    surf.vis = VisVTK.VisSurface()
    surf.render(colormap=cm.cool)
        