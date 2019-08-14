from collections import namedtuple
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

Solution = namedtuple('Solution',
                      'time trajectory step dimension')


# Plot a 2D phase portrait using the nth and mth component of the
# trajectory
def phasePortrait(sol, n, m):
    traj = sol.trajectory
    plt.plot(traj[:,n], traj[:,m])
    return 0

def subsample(sol, rate):
    traj = sol.trajectory[0::rate,:]
    time = sol.time[0::rate]

    return Solution(time, traj, sol.step, sol.dimension)

# Plot the nth component of the trajectory versus time
def plotSolution(sol, n, **kwargs):
    x = sol.trajectory[:,n]
    t = sol.time

    plt.plot(t, x, **kwargs)
    return 0

# Compare the norm of the separation of the given trajectories over time
# Both must be on the same time scale
def diffSolution(sol1, sol2):
    traj1 = sol1.trajectory
    traj2 = sol2.trajectory
    D = np.linalg.norm(traj1-traj2, axis=1)

    plt.plot(sol1.time, D)
    return D

# Plot the lorenz map (only useful for lorenz systems)
def lorenzMap(sol):
    traj = sol.trajectory
    zt = traj[:,2]
    z_max = zt[argrelextrema(zt, np.greater)[0]]
    zn = z_max[0:-1]
    zm = z_max[1:]

    plt.scatter(zn, zm)
    return 0

# Find the nearest vector in an array
def find_nearest(A, v):
    diff = np.linalg.norm(A - v, axis=1)
    idx = np.argmin(diff)
    return A[idx,:]

# Calculate the instances of time that the trajectory repeats
def recPoints(sol):
    traj = sol.trajectory
    p = find_nearest(traj, np.array([-2,0]))

    # Now calculate the number of times traj returns to p
    diff = np.linalg.norm(traj-p, axis=1)
    ids = np.where(diff < 1e-3)[0]

    return ids
