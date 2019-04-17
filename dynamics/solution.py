from collections import namedtuple
import matplotlib.pyplot as plt

Solution = namedtuple('Solution',
                      'time trajectory method step dimension')

def phasePortrait(sol, x, y):
    traj = sol.trajectory
    plt.plot(traj[:,x], traj[:,y])
    return 0

def plotSolution(sol, n):
    x = sol.trajectory[:,n]
    t = sol.time

    plt.plot(t, x)
    return 0
