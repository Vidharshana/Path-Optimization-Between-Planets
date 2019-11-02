# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:40:21 2019

@author: VidharshanaSivakumar
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

##Pseudocode for modelling the classical orbit of mercury
#Define  constants 
#Create lists for postion in x and y, velocity in x and y with the intial conditions given
#Compute the number of iterations that will be required to update the lists for the given length of time 

#Running the for loop for # of iterations calculated above
#For each iteration use the Euler-cromer method to compute the value of positions and velocities
#The rearranged equations to be used are as follows

#Vx_i+1= (-dt*G*M_s*X_i)/((X_i**2+Y_i**2)**(3/2)) + Vx_i   
#Vy_i+1= (-dt*G*M_s*Y_i)/((X_i**2+Y_i**2)**(3/2)) + Vy_i

#X_i+1= dt*Vx_i+1 + X_i
#Y_i+1= dt*Vy_i+1+ Y_i

#Add the updated values to the predefined lists

#Plotting the results
#Create a time axis to plot using the time length and time step given
#Plot x position vs time with labelled axes
#Plot y position vs time with labelled axes
#Plot x position vs y position




#Implementing code with data for Mercury (part C)


# Constants to be used in code
#Mass of Sun in Kilograms
M_s= 1

#1 astronomical unit(approximately distance between Sun and Earth)
Au= 1 #1.496*110**11m

#Gravitational constant
G= 39.5 #AU^3 / M_s*yr^2

#Alpha
a= 0.01 # AU**2

#Questions

#Rearranged Equations  for reference ( Using the Euler Cromer method)
#Vx_i+1= (-dt*G*M_s*X_i)/((X_i**2+Y_i**2)**(3/2)) + Vx_i   
#Vy_i+1= (-dt*G*M_s*Y_i)/((X_i**2+Y_i**2)**(3/2)) + Vy_i

#X_i+1= dt*Vx_i+1 + X_i
#Y_i+1= dt*Vy_i+1+ Y_i

#Initialize Storage Lists
X= [0.47] # X Position (Au)
Y= [0.0] # Y Position (Au)
V_x= [0.0] # X velocity (Au/year)
V_y= [8.17] #Y velocity (Au/year)

#Time assortments
T_t= 1 # total integration time is 1 year
dt= 0.0001  # time step is 0.0001 years
Steps= T_t/dt  # total number of iterations that the for loop will run for

#Integrating
for i in np.arange(0,int(Steps)):

    V_x1= (-dt*G*M_s*X[i])/((X[i]**2+Y[i]**2)**(3/2)) + V_x[i] #Computes value from existing entries using equation
    
    V_x.append(V_x1)   # Appends to initialized storage lists
    
    V_y1= (-dt*G*M_s*Y[i])/((X[i]**2+Y[i]**2)**(3/2)) + V_y[i]
    V_y.append(V_y1)
    
    X_1= dt*V_x[i+1]+X[i]
    X.append(X_1)
    
    Y_1=dt*V_y[i+1]+Y[i]
    Y.append(Y_1)
    

    
##Plotting the Results
T_ax= np.arange(0,1+dt,dt) # Time axis from 0 to 1 year in interval dt

#Plot of Y position vs X position
plt.figure(3)
plt.title("Y position vs X position")
plt.xlabel("X position (Au)")
plt.ylabel("Y position (Au)")
plt.plot(X,Y)
plt.savefig("Y_vs_X.pdf")
plt.show()
  