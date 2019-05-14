import numpy as np
import importlib
import methods
importlib.reload(methods)
from methods import *

mu = 1.5

def vanderpol_eq(state):
    x = state[0]
    y = state[1]
    return np.array([y, mu*(1-x**2)*y - x])

X0 = np.array([0.5, 0])
t = 100
h = 0.01

vp_rk4 = rk4(vanderpol_eq, X0, 0, t, h)
vp_rk2 = rk2(vanderpol_eq, X0, 0, t, h)
vp_euler = euler(vanderpol_eq, X0, 0, t, h)
vp_pc4 = adams_bashforth_moulton4(vanderpol_eq, X0, 0, t, h)
# vp_pc5 = adams_bashforth_moulton5(vanderpol_eq, X0, 0, t, h)
