import numpy as np
import math

x_trans , y_trans, z_trans = 0, 0, 0  #translation along x,y and z axis

#rotation along x,y and z axis
x_theta = 30 * math.pi / 180
y_theta = 30 * math.pi / 180
z_theta = 30 * math.pi / 180

co_ordinates = [2,3,0]

x_rotation = [ [ 1,0,0],[0 , math.cos(x_theta) , -math.sin(x_theta)],[0 , math.sin(x_theta) , math.cos(x_theta)],]
y_rotation = [ [math.cos(y_theta) ,0,math.sin(y_theta)],[0 , 1 , 0],[-math.sin(y_theta) , 0 , math.cos(y_theta)],]
z_rotation = [ [ math.cos(z_theta), -math.sin(z_theta),0],[math.sin(z_theta) , math.cos(z_theta) , 0],[0 , 0 , 1],]

#converting rotation matrices into numpy arrays
x_rotation = np.array(x_rotation)
y_rotation = np.array(y_rotation)
z_rotation = np.array(z_rotation)

rotation = ((x_rotation @ y_rotation) @ z_rotation)  # @ => matrix multiplication

transformation_matrix = [[rotation[0][0] , rotation[0][1],rotation[0][2],x_trans],
[rotation[1][0] , rotation[1][1],rotation[1][2],y_trans],
[rotation[2][0] , rotation[2][1],rotation[2][2],z_trans],
[0 ,0 ,0 ,1]]

co_ordinates.append(1.0)
co_ordinates = np.array(co_ordinates)

transformation_matrix = np.array(transformation_matrix)

solution_matrix = transformation_matrix @ co_ordinates

print('Solution Matrix: ')
print(solution_matrix)