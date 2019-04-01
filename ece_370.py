import numpy as np
import math as m

theta0 = 0.4
theta1 = 0.6
theta2 = 1.2
L0 = 0.3
L1 = 0.2
L2 = 0.1
LT = L0 + L1 + L2
ex = L2*m.cos(theta0+theta1+theta2) + L1*m.cos(theta0+theta1) + L0*m.cos(theta0)
ey = L2*m.sin(theta0+theta1+theta2) + L1*m.sin(theta0+theta1) + L0*m.sin(theta0)
thetaLH = (theta0+theta1+theta2)*((180/m.pi))
T0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T1_x = np.array([[m.cos(theta0), -m.sin(theta0), 0, 0], [m.sin(theta0), m.cos(theta0), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T1_y = np.array([[1, 0, 0, L0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T1 = np.dot(T1_x,T1_y)
T2_x = np.array([[m.cos(theta1), -m.sin(theta1), 0, 0], [m.sin(theta1), m.cos(theta1), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T2_y = np.array([[1, 0, 0, L1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T2 = np.dot(T2_x,T2_y)
T3_x = np.array([[m.cos(theta2), -m.sin(theta2), 0, 0], [m.sin(theta2), m.cos(theta2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T3_y = np.array([[1, 0, 0, L2], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T3 = np.dot(T3_x,T3_y)
T_1 = np.dot(T0,T1)
T_2 = np.dot(T_1,T2)
T = np.dot(T_2,T3)
print ("ex is equal to : ")
print(ex)
print ("ey matrix is equal to : ")
print(ey)
print ("ThetaLH in degrees is equal to : ")
print(thetaLH)
print ("The T matrix is equal to : ")
print(T)
TR = (T[0][0]) + (T[1][1]) + (T[2][2])
thetaM = m.acos(((TR - 1)/2))
thetaMd = thetaM*(180/m.pi)
print ("ThetaM in radians is equal to : ")
print(thetaM)
print("ThetaM in degrees is equal to : ")
print(thetaMd)
