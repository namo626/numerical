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

X0 = np.array([2.5, 0])

vanderpol = rk4(vanderpol_eq, X0, 0, 50, 0.2)
