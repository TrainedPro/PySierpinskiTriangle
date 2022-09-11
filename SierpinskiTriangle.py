import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

TriangleVertices = [(0.0, 0.0), (0.5, 1.0), (1.0, 0.0)]

x_list = []
y_list = []

figure, ax = plt.subplots()
ax.set_xlim = (0.0 , 1.0)
ax.set_ylim = (0.0 , 1.0)


line, = ax.plot(0.0, 0.0, 'g.')

def SierTri(n):
    x, y = random.choice(TriangleVertices)
    for _ in range(n):
        nx, ny = random.choice(TriangleVertices)

        x = (nx + x) / 2.0
        x_list.append(x)

        y = (ny + y) / 2.0
        y_list.append(y)

        line.set_xdata(x_list)
        line.set_ydata(y_list)

    return line,

animate = FuncAnimation(fig = figure,
                    func = SierTri,
                    frames=10,
                    interval=1)

# animate.save(r'animation.gif', fps=10)

plt.show()

print('Complete')


