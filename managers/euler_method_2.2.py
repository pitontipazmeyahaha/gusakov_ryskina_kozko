import models.classes as mod
import math
import matplotlib.pyplot as plt
import numpy as np
def f_x(t,x):
    return math.exp(t)*x
def f_y(t,y):
    return t*y
def move_through_space(time, h):
    t = h
    m = 0
    a = np.linspace(-4, 4, 9)
    x_s, y_s = np.meshgrid(a, a)
    velocity_fields = []
    for n in range(int(time / h)):
        space_points = []
        for i in range(9):
            for j in range(9):
                x = x_s[i, j]
                y = y_s[i, j]
                space_points.append(mod.SpacePoint(m, x, y, f_x(t,x), f_y(t,y), t))
                m += 1
            velocity_fields.append(mod.SpaceGrid(space_points))
        t += h
        return velocity_fields
def plot_velocity_fields(velocityfields):
    h = velocityfields[0].space_points[0].t
    t = h
    for n in range(len(velocityfields)):
        plt.figure(n)
        plt.suptitle('t = ' + str(t))
        m = 0
        coord_x = []
        coord_y = []
        v_x = []
        v_y = []
        for i in range(9):
            for j in range(9):
                coord_x.append(velocityfields[n].space_points[m].coord_x)
                coord_y.append(velocityfields[n].space_points[m].coord_y)
                v_x.append(velocityfields[n].space_points[m].velocity_x)
                v_y.append(velocityfields[n].space_points[m].velocity_y)
                m += 1
        plt.subplot(1, 2, 1)
        plt.quiver(coord_x, coord_y, v_x, v_y)
        for p in range(1,4):
            for q in range(1, 4):
                x = np.linspace(0.1,4,100 )
                d = t / math.exp(t)
                c = q * (p ** d)
                y = c * (x ** d)
                plt.subplot(1, 2, 2)
                plt.axis([-4, 4 , -4, 4])
                plt.plot(x,y)
        t += h
        plt.show()