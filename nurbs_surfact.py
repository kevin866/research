from geomdl import BSpline, utilities
from geomdl.visualization import VisPlotly

surf = BSpline.Surface()

surf.degree_u = 3
surf.degree_v = 2

control_points = [[0,0,0],[0,4,0],[0,8,-3],
                [2,0,6],[2,4,0],[2,8,0],
                [4,0,0],[4,4,0],[4,8,3],
                [6,0,0],[6,4,-3],[6,8,0]]

surf.set_ctrlpts(control_points, 4, 3)

surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, surf.ctrlpts_size_u)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, surf.ctrlpts_size_v)
surf.sample_size = 25
surf.evaluate()

vis_component = VisPlotly.VisSurface()
surf.vis = vis_component

surf.render()