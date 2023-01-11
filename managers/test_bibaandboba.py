import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
AutoMinorLocator)
import numpy as np
x = np.linspace(0, 10, 10)
y1 = 4*x
y2 = [i**2 for i in x]
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title('Графики зависимостей: y1=4*x, y2=x^2', fontsize=16)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y1, y2', fontsize=14)
ax.grid(which='major', linewidth=1.2)
ax.grid(which='minor', linestyle='--', color='gray', linewidth=0.5)
17
ax.scatter(x, y1, c='red', label='y1 = 4*x')
ax.plot(x, y2, label='y2 = x^2')
ax.legend()
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)
plt.show()

f_y(t, y), x, y, t))
            m += 1
    material_body = mod.MaterialBody(material_points)
    return material_body

def move_material_body(time,h,mb):
    point_trajectories = []
    c2 = 2/3
    c3 = 2/3
    a21 = 2/3
    a31 = -1/3
    a32 = 1
    b1 = 1/4
    b2 = 2/4
    b3 = 1/4
    for i in range(len(mb.material_points)):
        t = 0
        x_0 = mb.material_points[i].x_0
        y_0 = mb.material_points[i].y_0
        x_t = [x_0]
        y_t = [y_0]
        for n in range(int(time/h)+1):
            x_k = x_t[n]
            y_k = y_t[n]
            f_1x = f_x(t, x_k)
            f_2x = f_x(t + c2*h, x_k + h*a21*f_1x)
            f_3x = f_x(t + c3*h, x_k + h*a31*f_1x + h*a32*f_2x)
            f_1y = f_y(t, y_k)
            f_2y = f_y(t + c2 * h, y_k + h * a21 * f_1y)
            f_3y = f_y(t + c3 * h, y_k + h * a31 * f_1y + h * a32 * f_2y)
            x_t.append(x_k + h*(b1*f_1x + b2*f_2x + b3*f_3x))
            y_t.append(y_k + h * (b1 * f_1y + b2 * f_2y + b3 * f_3y))
            t += h