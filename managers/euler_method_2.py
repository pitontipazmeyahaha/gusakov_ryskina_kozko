import models.classes as mod
import math
import matplotlib.pyplot as plt
import numpy as np
def f_x(t,x):
    return - math.exp(t) * x
def f_y(t,y):
    return t * y
def move_through_space(time, h, grid_axis):
    t = h
    m = 0
    grid_length = grid_axis * 2 + 1
    a = np.linspace(-grid_axis, grid_axis, grid_length)
    x_s, y_s = np.meshgrid(a, a)
    velocity_fields = []
    for n in range(int(time / h) + 1):
        space_points = []
        for i in range(grid_length):
            for j in range(grid_length):
                x = x_s[i, j]
                y = y_s[i, j]
                space_points.append(mod.SpacePoint(m, x, y, f_x(t, x), f_y(t, y), t))
                m += 1
            velocity_fields.append(mod.SpaceGrid(space_points))
        t += h
        return velocity_fields
def plot_velocity_fields(velocity_fields, grid_axis):
    h = velocity_fields[0].space_points[0].t
    t = h
    grid_length = grid_axis * 2 + 1
    for n in range(len(velocity_fields)):
        plt.figure(n)
        plt.suptitle('t = ' + str(t))
        m = 0
        coord_x = []
        coord_y = []
        v_x = []
        v_y = []
        for i in range(grid_length):
            for j in range(grid_length):
                coord_x.append(velocity_fields[n].space_points[m].coord_x)
                coord_y.append(velocity_fields[n].space_points[m].coord_y)
                v_x.append(velocity_fields[n].space_points[m].velocity_x)
                v_y.append(velocity_fields[n].space_points[m].velocity_y)
                m += 1
        plt.subplot(1, 2, 1)
        plt.quiver(coord_x, coord_y, v_x, v_y)

        for i in range(0, 20):
            x1 = np.linspace(-grid_axis, -0.1, 100)
            x2 = np.linspace(0.1, grid_axis, 100)
            power = f_y(t, 1) / f_x(t, 1)
            diff_const = -i
            y1 = diff_const * pow(-x1, power)
            y2 = diff_const * pow(x2, power)

            plt.subplot(1, 2, 2)
            plt.axis([-grid_axis, grid_axis, -grid_axis, grid_axis])
            plt.plot(x1, y1)
            plt.plot(x2, y2)
        t += h
        plt.show()
        plt.savefig('поле_скоростей' + str(n) + '.png', format='png', dpi=1200)