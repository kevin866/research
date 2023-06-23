import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import open3d as o3d

# Read CSV
csvFileName = 'the_adas_lidar.xyz'
csvData = []
with open(csvFileName, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=' ')
    next(csvFile)
    for csvRow in csvReader:
        csvData.append(csvRow)

# Get X, Y, Z
csvData = np.array(csvData)
csvData = csvData.astype(np.float16)
X, Y, Z = csvData[:,0], csvData[:,1], csvData[:,2]
o3d.visualization.draw_geometries([csvData])

"""# Plot X,Y,Z
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(X, Y, Z, color='white', edgecolors='grey', alpha=0.5)
ax.scatter(X, Y, Z, c='red')
plt.show()"""
"""point_cloud = []
filename = "the_adas_lidar.xyz"
xyz = open(filename, "r")
xyz.readline()
xyz.readline()
xyz.readline()
line = xyz.readline()
print(line)
line.split()
point_cloud.append()
x, y, z, intensity, color = line.split()


xyz.close()"""