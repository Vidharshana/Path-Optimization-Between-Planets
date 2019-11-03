# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:40:21 2019

@author: VidharshanaSivakumar
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("dark_background")
import numpy.random

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
#X= [0.47] # X Position (Au)
#Y= [0.0] # Y Position (Au)
#V_x= [0.0] # X velocity (Au/year)
#V_y= [8.17] #Y velocity (Au/year)


n=5
X= [] # X Position (Au)
Y= [] # Y Position (Au)
V_x= [] # X velocity (Au/year)
V_y= [] #Y velocity (Au/year)

for q in np.arange(0,n):
    
    # These were selected  arbitrarily to produce random orbits as needed
    # Play around with these parameters as you desire to create different closed or open orbits
    x= 0.5 +np.random.rand()*1
#    x= np.random.rand()*0.5
    y= -1+ np.random.rand()*2
    v_x= -0.1+ np.random.rand()
    v_y=  6+0.2*np.random.rand()
#    v_y= 8*np.random.rand()
    
    X.append([x])
    Y.append([y])
    V_x.append([v_x])
    V_y.append([v_y])
#    


X1=[] # These will store  n trajectories for particles
Y1=[]
V1x=[]
V1y=[]  


#Time assortments
T_t= 2 # total integration time is 1 year- change this to close loops if needed
dt= 0.0001  # time step is 0.0001 years
Steps= T_t/dt  # total number of iterations that the for loop will run for

#Integrating
for j in range(len(V_y)):
    
    for i in np.arange(0,int(Steps)):
    
        V_x1= (-dt*G*M_s*X[j][i])/((X[j][i]**2+Y[j][i]**2)**(3/2)) + V_x[j][i] #Computes value from existing entries using equation
        
        V_x[j].append(V_x1)   # Appends to initialized storage lists
        
        V_y1= (-dt*G*M_s*Y[j][i])/((X[j][i]**2+Y[j][i]**2)**(3/2)) + V_y[j][i]
        V_y[j].append(V_y1)
        
        X_1= dt*V_x[j][i+1]+X[j][i]
        X[j].append(X_1)
        
        Y_1=dt*V_y[j][i+1]+Y[j][i]
        Y[j].append(Y_1)
        
        
        
#
#    
###Plotting the Results
#T_ax= np.arange(0,1+dt,dt) # Time axis from 0 to 1 year in interval dt

# This can be commented out if one just needs the orbits
for k in range(len(V_y)):
    plt.figure()
    plt.plot(0, 0, 'o', markersize=30, color='yellow')
    plt.plot(X[k],Y[k],"o",color="blue")
    plt.show()
#    
    
''' There was a variable defined, n, that controls the number of orbitals that are produced. X and Y are n sized lists with each 
element of the list being  size  T_t /dt  ( both variables defined above). To retrieve X and Y values for a particular planet, example
the first planet do X[0][i], Y[0][i]. '''






    
