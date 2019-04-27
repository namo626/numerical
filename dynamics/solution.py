from collections import namedtuple
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
