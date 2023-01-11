import managers.lagrange_method as lagr
import managers.euler_method_2 as euler

x_corner = 1
y_corner = 1
h = 0.5
time = 0.5
grid_axis = 3

body = lagr.create_material_body(x_corner, y_corner, h)
trajectory = lagr.move_material_body(time, h, body)

lagr.plot_trajectory(body, trajectory)

velocity_fields = euler.move_through_space(time, h, grid_axis)
euler.plot_velocity_fields(velocity_fields, grid_axis)
