import numpy as np
def read_xyz(fname):
  """ Reads xyz files """
  a2s  = np.loadtxt(fname, skiprows=2, usecols=[0], dtype=str)
  a2xyz = np.loadtxt(fname, skiprows=2, usecols=[1,2,3])
  assert len(a2s)==len(a2xyz)
  return a2s,a2xyz 
read_xyz('the_researcher_desk.xyz')