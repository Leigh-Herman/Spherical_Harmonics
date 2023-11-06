import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm

# Spherical coordinates
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 50)
theta, phi = np.meshgrid(theta, phi)

# Specify the quantum numbers (l and m)
l = 3  # l value
m = 2  # m value

# Calculate the spherical harmonics for the specified l and m values
Y_lm = np.real(sph_harm(m, l, theta, phi))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a function to update the plot in the animation
def update(frame):
    ax.clear()
    phi = np.linspace(0, np.pi, 50)
    theta = np.linspace(0, 2 * np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)
    Y_lm = np.real(sph_harm(m, l, theta, phi))
    X = np.sin(phi) * np.cos(theta)
    Y = np.sin(phi) * np.sin(theta)
    Z = np.cos(phi)
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.jet(Y_lm), rstride=1, cstride=1, alpha=0.6)
    ax.set_title(f"Spherical Harmonics Y_{l}_{m}")

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, repeat=False)

# Show the animation
plt.show()
