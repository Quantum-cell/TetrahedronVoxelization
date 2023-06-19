import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot_cube(ax, center, side_length, color='red'):
    x = center[0] - side_length / 2
    y = center[1] - side_length / 2
    z = center[2] - side_length / 2

    vertices = [[x, y, z],
                [x + side_length, y, z],
                [x + side_length, y + side_length, z],
                [x, y + side_length, z],
                [x, y, z + side_length],
                [x + side_length, y, z + side_length],
                [x + side_length, y + side_length, z + side_length],
                [x, y + side_length, z + side_length]]

    faces = [[0, 1, 2, 3],
             [4, 5, 6, 7],
             [0, 1, 5, 4],
             [1, 2, 6, 5],
             [2, 3, 7, 6],
             [3, 0, 4, 7]]

    # Plotting wireframe for edges
    ax.plot_wireframe(np.array([[vertices[i][0] for i in face] for face in faces]),
                      np.array([[vertices[i][1] for i in face] for face in faces]),
                      np.array([[vertices[i][2] for i in face] for face in faces]),
                      color='black')

    # Plotting the surfaces
    ax.plot_surface(np.array([[vertices[i][0] for i in face] for face in faces]),
                    np.array([[vertices[i][1] for i in face] for face in faces]),
                    np.array([[vertices[i][2] for i in face] for face in faces]),
                    color=color, alpha=0.6)

n = int(input("Enter a value for n: "))
side_length = 1

fig = plt.figure()

# first subplot - graph
ax = fig.add_subplot(111, projection='3d')

# Set axes limits dynamically based on the range of n values
ax.set_xlim([-side_length, n + side_length])
ax.set_ylim([-side_length, n + side_length])
ax.set_zlim([-side_length, n + side_length])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_box_aspect([1, 1, 1])  # Set aspect ratio to 1:1:1

def CT(layer, pos, n):
    if pos > layer:
        return CT(pos, layer, n)
    if layer + pos >= n:
        d = layer + pos - n + 1
        return CT(layer - d, pos - d, n)
    return 2**(layer-pos) * (2**(2*pos+1) - 1)

for z in range(n):
    for layer in range(n):
        for pos in range(n):
            binary_number = bin(CT(layer, pos, n))[2:].zfill(n)
            if binary_number[z] == '1':
                centerL1C = [pos, layer, z]
                plot_cube(ax, centerL1C, side_length, color='green')

plt.show()
