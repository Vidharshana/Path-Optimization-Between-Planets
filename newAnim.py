import random
import sys
import time
import tkinter as tk
import numpy as np
import math
import copy

G = 100000
m = 1
numShips = 6
numPlanets = 0

def move_to(x, y):
    #canvas.coords(object_simulated,x-10,y-10,x+10,y+10)
    canvas.create_oval(x-0.5,y-0.5,x+0.5,y+0.5, fill ="black", tags="dots")
    root.update()
    return


root = tk.Tk()                                  # spawns the window (which will be called "root")
root.title("OMG JUST WORK PLEASE")
canvas = tk.Canvas(root, width=1300, height=740) # creates a canvas to draw on
canvas.pack()                                   # spawns the squares and pack them in the canvas

#object_simulated = canvas.create_oval(400, 400, 405, 405, fill='white')
root.update()

def find_acceleration(x1,my_xs,q1,my_qs,real_distance):
    global G
    global m
    acceleration = 0
    direction = 1
    for i in range (len(my_xs)):
        try:
            distance = x1 - my_xs[i]
            if (distance < 0):
                direction = -1
            acceleration += (distance*G*q1*my_qs[i])/((real_distance[i]**3)*m)
        except ZeroDivisionError:
            acceleration += 0
    return acceleration

def find_velocity (vi,a):
    vf = vi + a*dt_prime
    return vf
def find_position(xi, vi):
    xf = xi + vi*dt_prime
    return xf



random.seed()

rand_x = random.randint(300, 700)
rand_y = random.randint(200, 400)
x_prime = [rand_x for i in range(6)]
y_prime = [rand_y for i in range(6)]
m_prime = 10
vx_prime = [random.randint(-350, 350) for i in range(6)]
vy_prime = [random.randint(-350, 350) for i in range(6)]
vx_init_copy = copy.deepcopy(vx_prime)
vy_init_copy = copy.deepcopy(vy_prime)
min_distances = [-1 for i in range(6)]

dt_prime = 0.01
total_time = [0 for i in range(6)]

mass_value = [0 for i in range(7)]
mass_x = [0 for i in range(7)]
mass_y = [0 for i in range(7)]
true_distances = [0 for i in range(7)]

#mass_simulated = []
def spawn_mass():
    global numPlanets
    numPlanets = random.randint(3,7)
    for i in range(numPlanets):
        my_choice = [random.randint(-20,-5) for l in range(4)]
        mass_value[i] = random.choice(my_choice)
        mass_x[i] = random.randint(100,1300)
        mass_y[i] = random.randint(100,700)
    if ((len(mass_x) - numPlanets - 1) > 0):
        for i in range(numPlanets, len(mass_x)-1):
            mass_value[i] = 0
            mass_x[i] = -200
            mass_y[i] = -200
    for i in range(len(mass_x)):
        if (i == (numPlanets-1)):
            s = canvas.create_oval(mass_x[i] - 5, mass_y[i] - 5, mass_x[i] + 5, mass_y[i] + 5, fill='yellow')
        else:
            s = canvas.create_oval(mass_x[i] - 5, mass_y[i] - 5, mass_x[i] + 5, mass_y[i] + 5, fill='red')
        #mass_posn = [mass_x[i], mass_y[i]]
        #mass_init_posn.append(mass_posn)
        #mass_simulated.append(s)
    root.update()
    return

spawn_mass()


for i in range(len(mass_x)):
    if (i == numPlanets - 1):
        s = canvas.create_oval(mass_x[i] - 5, mass_y[i] - 5, mass_x[i] + 5, mass_y[i] + 5, fill='blue')
    else:
        s = canvas.create_oval(mass_x[i] - mass_value[i]/2, mass_y[i] - mass_value[i]/2, mass_x[i] + mass_value[i]/2, mass_y[i] + mass_value[i]/2, fill='red')
    #mass_simulated.append(s)
root.update()

resumeAnimation = [1 for i in range(6)]
for i in range (0,2500):
    for k in range(0, 6):
        if (resumeAnimation[k] == 0):
            continue
        else:
            move_to(x_prime[k],y_prime[k])
            total_time[k] += dt_prime

            for j in range (len(mass_x)):
                true_distances[j] = math.sqrt((mass_x[j]-x_prime[k])**2 + (mass_y[j]-y_prime[k])**2)
    	        #print("Euclidean distance to from spaceship " + str(k) + " to planet " + str(j) + " is " + str(1000*true_distances[j]) + " km")
                if (true_distances[j] <= 15):
    	            resumeAnimation[k] = 0
                if (j == numPlanets - 1):
                    if (min_distances[k] == -1):
                        min_distances[k] = true_distances[j]
                    elif (true_distances[j] < min_distances[k]):
                        min_distances[k] = true_distances[j]
                    else:
                        continue

            ax_prime = find_acceleration(x_prime[k],mass_x,m_prime,mass_value,true_distances)
            vx_prime[k] = find_velocity(vx_prime[k],ax_prime)
            x_prime[k] = find_position(x_prime[k],vx_prime[k])
            ay_prime = find_acceleration(y_prime[k],mass_y,m_prime,mass_value,true_distances)
            vy_prime[k] = find_velocity(vy_prime[k],ay_prime)
            y_prime[k] = find_position(y_prime[k],vy_prime[k])
            time.sleep(0.001)

canvas.delete("dots");
print(min_distances)
print(total_time)

min_path_indx_1 = 0
min_path_indx_2 = 0

for i in range(numShips):
    if (min_distances[min_path_indx_1] <= min_distances[i]):
        if (min_distances[min_path_indx_2] <= min_distances[i]):
            continue
        else:
            min_path_indx_2 = i
    else:
        min_path_indx_2 = min_path_indx_1
        min_path_indx_1 = i

print(min_distances[min_path_indx_1])
print(min_distances[min_path_indx_2])

chosen_path_index = 0
if (total_time[min_path_indx_1] < total_time[min_path_indx_2]):
    chosen_path_index = min_path_indx_1
else:
    chosen_path_index = min_path_indx_2

print(chosen_path_index);
print(total_time[chosen_path_index]);

x_prime = [rand_x for i in range(6)]
y_prime = [rand_y for i in range(6)]

vx_prime = [random.randint(vx_init_copy[chosen_path_index] - (350/2), vx_init_copy[chosen_path_index] + (350/2)) for i in range(6)]
vy_prime = [random.randint(vy_init_copy[chosen_path_index] - (350/2), vy_init_copy[chosen_path_index] + (350/2)) for i in range(6)]

vx_init_copy = copy.deepcopy(vx_prime)
vy_init_copy = copy.deepcopy(vy_prime)
min_distances = [-1 for i in range(6)]
total_time = [0 for i in range(6)]

resumeAnimation = [1 for i in range(6)]
for i in range (0,2500):
    for k in range(0, 6):
        if (resumeAnimation[k] == 0):
            continue
        else:
            move_to(x_prime[k],y_prime[k])
            total_time[k] += dt_prime

            for j in range (len(mass_x)):
                true_distances[j] = math.sqrt((mass_x[j]-x_prime[k])**2 + (mass_y[j]-y_prime[k])**2)
    	        #print("Euclidean distance to from spaceship " + str(k) + " to planet " + str(j) + " is " + str(1000*true_distances[j]) + " km")
                if (true_distances[j] <= 15):
                    resumeAnimation[k] = 0
                if (j == numPlanets - 1):
                    if (min_distances[k] == -1):
                        min_distances[k] = true_distances[j]
                    elif (true_distances[j] < min_distances[k]):
                        min_distances[k] = true_distances[j]
                    else:
                        continue

            ax_prime = find_acceleration(x_prime[k],mass_x,m_prime,mass_value,true_distances)
            vx_prime[k] = find_velocity(vx_prime[k],ax_prime)
            x_prime[k] = find_position(x_prime[k],vx_prime[k])
            ay_prime = find_acceleration(y_prime[k],mass_y,m_prime,mass_value,true_distances)
            vy_prime[k] = find_velocity(vy_prime[k],ay_prime)
            y_prime[k] = find_position(y_prime[k],vy_prime[k])
            time.sleep(0.001)

canvas.delete("dots");
print(min_distances)
print(total_time)

min_path_indx_1 = 0
min_path_indx_2 = 0

for i in range(numShips):
    if (min_distances[min_path_indx_1] <= min_distances[i]):
        if (min_distances[min_path_indx_2] <= min_distances[i]):
            continue
        else:
            min_path_indx_2 = i
    else:
        min_path_indx_2 = min_path_indx_1
        min_path_indx_1 = i

print(min_distances[min_path_indx_1])
print(min_distances[min_path_indx_2])

chosen_path_index = 0
if (total_time[min_path_indx_1] < total_time[min_path_indx_2]):
    chosen_path_index = min_path_indx_1
else:
    chosen_path_index = min_path_indx_2

print(chosen_path_index);
print(total_time[chosen_path_index]);

x_prime = [rand_x for i in range(6)]
y_prime = [rand_y for i in range(6)]

vx_prime = [random.randint(vx_init_copy[chosen_path_index] - (350/2), vx_init_copy[chosen_path_index] + (350/2)) for i in range(6)]
vy_prime = [random.randint(vy_init_copy[chosen_path_index] - (350/2), vy_init_copy[chosen_path_index] + (350/2)) for i in range(6)]

vx_init_copy = copy.deepcopy(vx_prime)
vy_init_copy = copy.deepcopy(vy_prime)
min_distances = [-1 for i in range(numShips)]
total_time = [0 for i in range(6)]
resumeAnimation = [1 for i in range(6)]
for i in range (0,2500):
    for k in range(0, 6):
        if (resumeAnimation[k] == 0):
            continue
        else:
            move_to(x_prime[k],y_prime[k])
            total_time[k] += dt_prime

            for j in range (len(mass_x)):
                true_distances[j] = math.sqrt((mass_x[j]-x_prime[k])**2 + (mass_y[j]-y_prime[k])**2)
    	        #print("Euclidean distance to from spaceship " + str(k) + " to planet " + str(j) + " is " + str(1000*true_distances[j]) + " km")
                if (true_distances[j] <= 15):
                    resumeAnimation[k] = 0
                if (j == numPlanets - 1):
                    if (min_distances[k] == -1):
                        min_distances[k] = true_distances[j]
                    elif (true_distances[j] < min_distances[k]):
                        min_distances[k] = true_distances[j]
                    else:
                        continue

            ax_prime = find_acceleration(x_prime[k],mass_x,m_prime,mass_value,true_distances)
            vx_prime[k] = find_velocity(vx_prime[k],ax_prime)
            x_prime[k] = find_position(x_prime[k],vx_prime[k])
            ay_prime = find_acceleration(y_prime[k],mass_y,m_prime,mass_value,true_distances)
            vy_prime[k] = find_velocity(vy_prime[k],ay_prime)
            y_prime[k] = find_position(y_prime[k],vy_prime[k])
            time.sleep(0.001)


tk.mainloop();
