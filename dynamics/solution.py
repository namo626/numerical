from collections import namedtuple
import numpy as np
import matplotlib.pyplot as plt

Solution = namedtuple('Solution',
                      'time trajectory step dimension')


# Plot a 2D phase portrait using the nth and mth component of the
# trajectory
def phasePortrait(sol, n, m):
    traj = sol.trajectory
    plt.plot(traj[:,n], traj[:,m])
    return 0


# Plot the nth component of the trajectory versus time
def plotSolution(sol, n):
    x = sol.trajectory[:,n]
    t = sol.time

    plt.plot(t, x)
    return 0

# Compare the norm of the separation of the given trajectories over time
# Both must be on the same time scale
def diffSolution(sol1, sol2):
    traj1 = sol1.trajectory
    traj2 = sol2.trajectory
    D = np.linalg.norm(traj1-traj2, axis=1)

    plt.plot(sol1.time, D)
    return 0
