import importlib
import solution
import methods
importlib.reload(solution)
importlib.reload(methods)
from solution import *
from methods import *
from functools import partial


def lorenz_eq(sigma, rho, beta, state):
    x = state[0]; y = state[1]; z = state[2]
    return np.array([sigma*(y-x),
                     x*(rho-z) - y,
                     x*y - beta*z])

# standard parameters
F = partial(lorenz_eq, 10, 28, 8/3)
# initial condition
X0 = np.array([1.0, 1.0, 1.0])

t0 = 0.0
tf = 40.0
h = 0.01

lorenz_rk4 = rk4(F, X0, t0, tf, h)
lorenz_euler = euler(F, X0, t0, tf, h)
