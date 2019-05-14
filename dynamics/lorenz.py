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

F = partial(lorenz_eq, 10, 21, 8/3)
# X0 = np.array([5, 2, 8])
X0 = np.array([2, 10, 6])

t0 = 0.0
tf = 100.0
h = 0.01

lorenz_rk4 = rk4(F, X0, t0, tf, h)
lorenz_rk2 = rk2(F, X0, t0, tf, h)
lorenz_euler = euler(F, X0, t0, tf, h)
lorenz_pc2 = adams_bashforth_moulton2(F, X0, t0, tf, h)
lorenz_pc4 = adams_bashforth_moulton4(F, X0, t0, tf, h)
# lorenz_pc5 = adams_bashforth_moulton5(F, X0, t0, tf, h)
