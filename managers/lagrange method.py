import models.classes as mod
import math
import matplotlib.pyplot as plt
import numpy as np

def f_x(t,x):
    return math.exp(t)
def f_y(t,y):
    return t

def create_material_body(x_c,y_c,h):
    t = 0
    m = 0
    material_points = []
    for i in range(int(2/h)+1):
        for j in range(int(2/h)+1):
            x = x_c + j*h
            y = y_c + i*h
            material_points.append(mod.MaterialPoint(m,x,y,f_x(t,x),f_y(t,y),x,y,t))
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
        point_trajectories.append(mod.PointTrajectory(mb.material_points[i], x_t, y_t))
    body_trajectory = mod.BodyTrajectory(point_trajectories, mb)
    return body_trajectory

def plot_trajectory(mb, tr):
    for i in range(len(mb.material_points)):
        plt.plot(mb.material_points[i].coord_x, mb.material_points[i].coord_y, 'g')
    for i in range(len(mb.material_points)):
        plt.plot(tr.point_trajectories[i].x, tr.point_trajectories[i].y, 'b')
    for i in range(len(mb.material_points)):
        time = len(tr.point_trajectories[i].x)-1
        plt.plot(tr.point_trajectories[i].x[time], tr.point_trajectories[i].y[time], 'r')
    plt.axis('equal')
    plt.grid()
    plt.savefig('assets/plot_trajectory.png', format='png', dpi=300)