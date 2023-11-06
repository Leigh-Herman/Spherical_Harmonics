import numpy as np
from scipy.special import sph_harm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters for the spherical harmonics
l = 2 # Azimuthal quantum number
m = 1 # Magnetic quantum number

# Create a grid of points on the unit sphere
theta, phi = np.mgrid[0.0:2.0 * np.pi:100j, 0.0:np.pi:50j]

# Caluculate the spherical harmonic values at each point on the grid
r = np.abs(sph_harm(m, l, theta, phi))

# Convert spherical coordinates to Cartesian coordinates
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# Create a #d plot to visulaize the pherical harmoncs
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plot = ax.plot_surface( x, y, z, rstride=1, cstride=1, cmap=plt.get_cmap('jet'), linewidth=0, antialiased=False, alpha=0.5)

# Set plot labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Spherical Harmonic (l,m) = (' + str(l) + ',' + str(m) + ')')

plt.show()