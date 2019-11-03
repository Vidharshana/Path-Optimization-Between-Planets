import random
import sys
import time
import tkinter as tk
import numpy as np
import math

ke = 10000
m = 1

def move_to(x, y):
    canvas.coords(object_simulated,x-10,y-10,x+10,y+10)
    canvas.create_oval(x-0.5,y-0.5,x+0.5,y+0.5, fill ="black")
    root.update()
    return


root = tk.Tk()                                  # spawns the window (which will be called "root")
root.title("Simulation of Equation received")
canvas = tk.Canvas(root, width=1300, height=740) # creates a canvas to draw on
canvas.pack()                                   # spawns the squares and pack them in the canvas

object_simulated = canvas.create_oval(400, 400, 405, 405, fill='white')
root.update()

def find_acceleration(x1,my_xs,q1,my_qs,real_distance):
    global ke
    global m
    acceleration = 0
    direction = 1
    for i in range (len(my_xs)):
        try:
            distance = x1 - my_xs[i] 
            print(distance)
            print("Is the distance \n")
            if (distance < 0):
                direction = -1
            acceleration += (distance*ke*q1*my_qs[i])/((real_distance[i]**3)*m)
        except ZeroDivisionError:
            acceleration += 0
    print("Calculating acceleration " + str(acceleration))
    #print(ke,x1,q1,my_xs,my_qs,m)
    return acceleration

def find_velocity (vi,a):
    vf = vi + a*dt_prime
    print("Calculating velocity " + str(vf))
    return vf
def find_position(xi, vi):
    xf = xi + vi*dt_prime
    print("Calculating position " + str(xf))
    return xf



random.seed()


x_prime = [500, 500, 500, 500, 500, 500]
y_prime = [500, 500, 500, 500, 500, 500]
q_prime = 10
vx_prime = [random.randint(-350, 350) for i in range(6)]
vy_prime = [random.randint(-350, 350) for i in range(6)]
dt_prime = 0.01
energy_loss_x_prime = 0.99
energy_loss_y_prime = 0.99

charges_value = [-10,-5, -10, random.randint(-20,-5),0,0,0]
charges_x = [600,500,200, random.randint(100,1000),0,0,0]
charges_y = [500,400,400,random.randint(100,700),0,0,0]
true_distances = [0,0,0,0,0,0,0]

def spawn_charges():
    j = random.randint(3,7)
    for i in range(j):
        my_choice = [random.randint(-20,-5) for l in range(4)]
        charges_value[i] = random.choice(my_choice)
        charges_x[i] = random.randint(100,1300)
        charges_y[i] = random.randint(100,700)
    if ((len(charges_x) - j - 1) > 0):
        for i in range(j, len(charges_x)-1):
            charges_value[i] = 0
            charges_x[i] = -200
            charges_y[i] = -200
    for i in range(len(charges_x)):
        if (charges_value[i] < 0):
            s = canvas.create_oval(charges_x[i] - 5, charges_y[i] - 5, charges_x[i] + 5, charges_y[i] + 5, fill='red')
            charges_simulated.append(s)
        else:
            s = canvas.create_oval(charges_x[i] - 5, charges_y[i] - 5, charges_x[i] + 5, charges_y[i] + 5, fill='blue')
            charges_simulated.append(s)
    print(str(charges_x[i])+str(charges_y[i]) + "those are the coordinates" )
    root.update()
    return


charges_simulated = []

spawn_charges()
for i in range(len(charges_x)):
    s = canvas.create_oval(charges_x[i] - charges_value[i]/2, charges_y[i] - charges_value[i]/2, charges_x[i] + charges_value[i]/2, charges_y[i] + charges_value[i]/2, fill='red')
    charges_simulated.append(s)
    print(str(charges_x[i])+str(charges_y[i]) + "those are the coordinates" )
root.update()

skip = 0
for i in range (0,5000):
    for k in range(0, 6):
	    move_to(x_prime[k],y_prime[k])
	    print("this is x_prime \n")

	    for j in range (len(charges_x)):
	        true_distances[j] = math.sqrt((charges_x[j]-x_prime[k])**2 + (charges_y[j]-y_prime[k])**2)
	        print("Euclidean distance to planet " + str(j) + " is " + str(true_distances[j]) + " km")
	        if (true_distances[j] <= 15):
	            skip = 1

	    if (skip ==1):
	        vx_prime[k] = -vx_prime[k]*energy_loss_x_prime
	        vy_prime[k] = -vy_prime[k]*energy_loss_y_prime
	        x_prime[k] = find_position(x_prime[k],vx_prime[k])
	        y_prime[k] = find_position(y_prime[k],vy_prime[k])
	        print("Reversing position")
	        time.sleep(0.001)
	        skip = 0
	        continue

	    ax_prime = find_acceleration(x_prime[k],charges_x,q_prime,charges_value,true_distances)
	    vx_prime[k] = find_velocity(vx_prime[k],ax_prime)
	    x_prime[k] = find_position(x_prime[k],vx_prime[k])
	    print("this is x_prime :" + str(x_prime[k]))
	    ay_prime = find_acceleration(y_prime[k],charges_y,q_prime,charges_value,true_distances)
	    vy_prime[k] = find_velocity(vy_prime[k],ay_prime)
	    y_prime[k] = find_position(y_prime[k],vy_prime[k])
	    print("this is y_prime" + str(y_prime[k]))
	    time.sleep(0.001)

