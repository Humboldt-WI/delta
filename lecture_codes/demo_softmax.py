# Example of the softmax function for two-class classification
# Source: https://peterroelants.github.io/posts/cross-entropy-softmax/

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Generate some input data corresponding to z values in 2d
nb_of_zs = 250
zs = np.linspace(-5, 5, num=nb_of_zs)
zs_1, zs_2 = np.meshgrid(zs, zs)


def softmax(z):
    """ Softmax function """
    return np.exp(z) / np.sum(np.exp(z))


# Invoke softmax function with every combination of z1 and z2
# assuming we have two classes
out = np.zeros((nb_of_zs, nb_of_zs, 2))
for i in range(nb_of_zs):
    for j in range(nb_of_zs):
        out[i, j, :] = softmax(np.asarray([zs_1[i, j], zs_2[i, j]]))
print(out.shape)

# Plot the output surface for one of the classes
with sns.axes_style("whitegrid"):
    fig = plt.figure(figsize=(6, 4))
    # Plot the loss function surface for t=1
    ax = fig.gca(projection='3d')
surf = ax.plot_surface(
    zs_1, zs_2, out[:, :, 0], linewidth=0, cmap=cm.viridis)
ax.view_init(elev=30, azim=70)
cbar = fig.colorbar(surf)
ax.set_xlabel('$z_1$', fontsize=10)
ax.set_ylabel('$z_2$', fontsize=10)
ax.set_zlabel('$P(y=1|\mathbf{z})$', fontsize=10)
# cbar.ax.set_ylabel('$P(c=1|\mathbf{z})$', fontsize=12)
plt.show();
