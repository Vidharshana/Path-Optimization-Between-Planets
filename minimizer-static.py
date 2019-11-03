import numpy as np
import matplotlib.pyplot as plt

# generate positions and thrusts
init_pos = np.array([0,0])
end_pos = np.array([1,0])
#planet_positions = [[1,0], [0.5, 0.9], [0.7, -0.5]]
#planet_piositions = [[1,0], [0.5, 0.5], [0.5, -0.5]]
#planet_positions = [[1,0], [0.5, 0.5]]
#planet_positions = [[1, 0], [2, 0], [3, 0]]
#planet_masses = [3, 2, 1]
planet_positions = [[1,0]]
planet_masses = [1]

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
    def get_force_on_ship(pos):
        force = 0
        for i in range(len(planet_poses)):
            force += -planet_masses[i]*(pos - planet_poses[i])/(np.linalg.norm(pos-planet_poses[i])+0.0001)**3
        return force
    while t < end_time:
        #print(pos, t)
        force = get_force_on_ship(pos)
        vel = vel + force*dt
        pos = pos + vel*dt
        trajectory[t] = pos
        distances[t] = np.linalg.norm(pos - end_pos)
        t += dt
    time_min = list(distances.keys())[list(distances.values()).index(np.min(list(distances.values())))]
    # only return trajectory up to minimum value
    for t in list(trajectory.keys()):
        if t > time_min:
            del trajectory[t]
    return trajectory, np.min(list(distances.values())), time_min, thrust

thrusts = get_thrusts([0,2*np.pi], [0,5])
plt.figure(figsize=[10,7])
for i in range(10):
    plt.subplot(3, 4, i+1)
    print("iteration", i)
    # convert thrusts to np array
    thrusts = np.array(thrusts)
    plt.xlim(-0.5, 1.5)
    plt.ylim(-1, 1)
    meta_trajectories = []
    for thrust in thrusts:
        trajectory, how_close, at_what_time, at_what_thrust = simulate(thrust, init_pos, planet_positions, 1)
        xs, ys = zip(*list(trajectory.values()))
        plt.plot(xs, ys)
        print(how_close, at_what_time)
        meta_trajectories.append((how_close, at_what_time, at_what_thrust))

    plt.scatter(*zip(*planet_positions), s=20, c="blue")
    print(planet_positions)
    #plt.savefig("orbits-test-case/orbits"+str(i)+".png")
    #plt.savefig("orbits-weird-case/less-acc-orbits"+str(i)+".png")
    #plt.savefig("orbits-series3/orbits"+str(i)+".png")
    #plt.savefig("orbits-series2/orbits"+str(i)+".png")
    #plt.savefig("new-orbits"+str(i)+".png")
    #plt.show()
    #plt.cla()

    # meta_trajectories analysis
    meta_trajectories.sort(key = lambda tup: tup[0])
    top_trajes = meta_trajectories[:5]  
    top_trajes.sort(key= lambda tup: tup[1])
    top_traj = top_trajes[0][2]
    new_angle_range = [top_traj[0]-(np.pi/(2**i)),top_traj[0]+(np.pi/(2**i))]
    new_magnitude_range = [top_traj[1] - (2.5/(2**i)),top_traj[1] + (2.5/(2**i))]
    thrusts = get_thrusts(new_angle_range, new_magnitude_range)
    
plt.savefig("orbits-test-case/orbit_subplot.png")
