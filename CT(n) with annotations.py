import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sympy import isprime

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
                    color=color, alpha=0.5)

fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)
ax2.axis('off')
n = int(input("Enter a value for n: "))
side_length = 1

ax.set_xlim([-side_length, n + side_length])
ax.set_ylim([-side_length, n + side_length])
ax.set_zlim([-side_length, n + side_length])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_box_aspect([1, 1, 1])

ax2.axis('off')

bbox_props = dict(boxstyle='square,pad=4.2', edgecolor='white', facecolor='white', alpha=0)

count_list_pos = []
count_list_layer = []
x_count = 0.1
x_prime = 0.55
y_count = 0.85

def CT(layer, pos, n):
    if pos > layer:
        return CT(pos, layer, n)
    if layer + pos >= n:
        d = layer + pos - n + 1
        return CT(layer - d, pos - d, n)
    return 2 ** (layer - pos) * (2 ** (2 * pos + 1) - 1)

for z in range(n):
    for layer in range(n):
        for pos in range(n):
            binary_number = bin(CT(layer, pos, n))[2:].zfill(n)
            if binary_number[z] == '1':
                count_list_pos.append(1)
                centerL1C = [pos, layer, z]
                plot_cube(ax, centerL1C, side_length, color='green')
        count_list_layer.append(sum(count_list_pos))
        count_list_pos = []
    count_sum_layer = sum(count_list_layer)
    count_text = 'layer ' + str(z + 1) + ' = ' + str(count_sum_layer)
    y_count -= 1 / (n + 1)
    ax2.text(x_count, y_count, count_text, ha='left', va='center', wrap=True, bbox=bbox_props, fontsize=8)

    if isprime(count_sum_layer):
        prime_text = 'Prime'
        ax2.text(x_prime, y_count, prime_text, ha='left', va='center', wrap=True, bbox=bbox_props, fontsize=8)
    else:
        not_prime_text = 'Not Prime'
        ax2.text(x_prime, y_count, not_prime_text, ha='left', va='center', wrap=True, bbox=bbox_props, fontsize=8)

    count_list_layer = []

plt.show()

print("Program Exited")
