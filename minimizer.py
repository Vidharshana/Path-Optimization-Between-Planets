import numpy as np
import matplotlib.pyplot as plt

# generate positions and thrusts
init_pos = np.array([0,0])
end_pos = np.array([1,0])

#test cases
#planet_positions = [[1,0], [0.5, 0.9], [0.7, -0.5]]
#planet_positions = [[1,0], [0.5, 0.5], [0.5, -0.5]]
#planet_positions = [[1,0], [0.5, 0.5]]
#planet_positions = [[1, 0], [2, 0], [3, 0]]
#planet_masses = [1, 1]
#planet_positions = [[1,0]]

# first position is the sun
planet_positions = np.array([[1, 0], [1, -0.5]])
planet_masses = np.array([5, 1])
ending_poses = []

def simulate_planets(end_time):
    planet_velocities=np.array([[0,0], [3, 0]])
    dt = 0.001
    # list of dicts of planets
    planet_poses = []
    # fill out sun's trajectory (constant)
    t = 0
    sun_traj = {}
    while t < end_time:
        sun_traj[t] = planet_positions[0]
        t += dt
    planet_poses.append(sun_traj)
    
    
    for i in range(1,len(planet_positions)):
        planet_trajectory = {}
        t = 0
        vel = planet_velocities[i]
        pos = planet_positions[i]
        sun_pos = planet_positions[0]
        while t < end_time:
            force = -planet_masses[0]*(pos-sun_pos)/(np.linalg.norm(pos-sun_pos)+0.0001)**3
            vel = vel + force*dt
            pos = pos + vel*dt
            planet_trajectory[t] = pos
            t += dt
        planet_poses.append(planet_trajectory)
    return planet_poses

planet_poses = simulate_planets(5)
end_pos = planet_poses[-1]

# get thrusts in polar coordinates
def get_thrusts(angle_range, mag_range):
    thrusts =[]
    angles = np.linspace(angle_range[0], angle_range[1], 10)
    magnitudes = np.linspace(mag_range[0], mag_range[1], 10)
    for mag in magnitudes:
        for angle in angles:
            thrusts.append([angle, mag])
    return thrusts

## iterate code from this point on

def simulate(thrust, init_pos, planet_poses, end_time ):
    pos = init_pos
    # convert thrust to cartesian
    vel = [thrust[1]*np.cos(thrust[0]),thrust[1]*np.sin(thrust[0])]
    t = 0
    dt = 0.001
    trajectory = {}
    distances = {}
    def get_force_on_ship(pos, t):
        force = 0
        for i in range(len(planet_positions)):
            force += -planet_masses[i]*(pos - planet_poses[i][t])/(np.linalg.norm(pos-planet_poses[i][t])+0.0001)**3
        return force
    while t < end_time:
        #print(pos, t)
        force = get_force_on_ship(pos,t)
        vel = vel + force*dt
        pos = pos + vel*dt
        trajectory[t] = pos
        distances[t] = np.linalg.norm(pos - end_pos[t])
        t += dt
    time_min = list(distances.keys())[list(distances.values()).index(np.min(list(distances.values())))]
    # only return trajectory up to minimum value
    for t in list(trajectory.keys()):
        if t > time_min:
            del trajectory[t]
    return trajectory, np.min(list(distances.values())), time_min, thrust

thrusts = get_thrusts([0,2*np.pi], [0,5])
for i in range(10):
    print("iteration", i)
    # convert thrusts to np array
    thrusts = np.array(thrusts)
    plt.xlim(-0.5, 1.5)
    plt.ylim(-1, 1)
    meta_trajectories = []
    for thrust in thrusts:
        trajectory, how_close, at_what_time, at_what_thrust = simulate(thrust, init_pos, planet_poses, 5)
        xs, ys = zip(*list(trajectory.values()))
        plt.plot(xs, ys)
        print(how_close, at_what_time)
        meta_trajectories.append((how_close, at_what_time, at_what_thrust))

    
    #calculate final positions of objects AHHH it shouldnt be this hard!!:
    #final_xs = []
    #final_ys = [] 
    #for k in range(len(planet_positions)):
    #    t = max(list(planet_poses[k].keys()))
    #    final_xs.append(planet_poses[k][t][0])
    #    final_ys.append(planet_poses[k][t][1])
    #plt.scatter(final_xs, final_ys, s=25, c="blue")

    # plot the trajectory of the planets
    for k in range(len(planet_positions)):
        plt.plot(*zip(*list(planet_poses[k].values())))

    #plt.scatter(*zip(*planet_positions), s=20, c="blue")
    #plt.savefig("orbits-test-case/orbits"+str(i)+".png")
    #plt.savefig("orbits-weird-case/less-acc-orbits"+str(i)+".png")
    #plt.savefig("orbits-series3/orbits"+str(i)+".png")
    #plt.savefig("orbits-series2/orbits"+str(i)+".png")
    #plt.savefig("orbits-series1/orbits"+str(i)+".png")
    plt.savefig("orbits-moving-objects/orbits"+str(i)+".png")
    #plt.show()
    plt.cla()

    # meta_trajectories analysis
    meta_trajectories.sort(key = lambda tup: tup[0])
    top_trajes = meta_trajectories[:5]  
    top_trajes.sort(key= lambda tup: tup[1])
    top_traj = top_trajes[0][2]
    
    # plot the position of the planet at closest approach
    time_at_closest = top_trajes[0][1]
    closest_xs = []
    closest_ys = [] 
    for k in range(len(planet_positions)):
        #t = max(list(planet_poses[k].keys()))
        closest_xs.append(planet_poses[k][time_at_closest][0])
        closest_ys.append(planet_poses[k][time_at_closest][1])
    plt.scatter(closest_xs, closest_ys, s=100, c="blue", marker="*")
    
    new_angle_range = [top_traj[0]-(np.pi/(2**i)),top_traj[0]+(np.pi/(2**i))]
    new_magnitude_range = [top_traj[1] - (2.5/(2**i)),top_traj[1] + (2.5/(2**i))]
    thrusts = get_thrusts(new_angle_range, new_magnitude_range)
    

