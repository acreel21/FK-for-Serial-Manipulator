clear all;
close all;
clc;
theta0 = 0.4;
theta1 = 0.6;
theta2 = 1.2;
L0 = 0.3;
L1 = 0.2;
L2 = 0.1;
LT = L0+L1+L2;
ex = L2*cos(theta0+theta1+theta2) + L1*cos(theta0+theta1) + L0*cos(theta0)
ey = L2*sin(theta0+theta1+theta2) + L1*sin(theta0+theta1) + L0*sin(theta0)
thetaLH = rad2deg(0.4+0.6+1.2)
T0 = [1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1];
T1 = [cos(theta0) -sin(theta0) 0 0; sin(theta0) cos(theta0) 0 0; 0 0 1 0; 0 0 0 1]*[1 0 0 L0; 0 1 0 0; 0 0 1 0; 0 0 0 1];
T2 =[cos(theta1) -sin(theta1) 0 0; sin(theta1) cos(theta1) 0 0; 0 0 1 0; 0 0 0 1]*[1 0 0 L1; 0 1 0 0; 0 0 1 0; 0 0 0 1];
T3 = [cos(theta2) -sin(theta2) 0 0; sin(theta2) cos(theta2) 0 0; 0 0 1 0; 0 0 0 1]*[1 0 0 L2; 0 1 0 0; 0 0 1 0; 0 0 0 1];
T = T0*T1*T2*T3
TR = diag(T);
thetaM = rad2deg(acos(((TR(1)+TR(2)+TR(3))-1)/2))