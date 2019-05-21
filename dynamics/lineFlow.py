import numpy as np
import math
import matplotlib.pyplot as plt
import importlib
import solution
importlib.reload(solution)
from solution import *

def general_method(stepper, F, init, t0, tf, h):
    t     = np.arange(t0, tf+h, h)
    steps = t.shape[0] - 1
    dim   = init.shape[1]
    X     = np.zeros((steps+1, dim))

    # initializing the array with the given initial state
    init_length = init.shape[0]
    X[0:init_length, :] = init

    # start integrating after the last initial vector
    for i in range(init_length-1, steps):
        X[i+1, :] = stepper(F, X, i, h)

    return Solution(t, X, h, dim)


def singlestep_method(stepper, F, X0, t0, tf, h):
    init = np.reshape(X0, (1, X0.shape[0]))
    return general_method(stepper, F, init, t0, tf, h)


def multistep_method(N, gen, stepper, F, X0, t0, tf, h):
    # generate the first N steps (including X0) using a single-step method, e.g. RK4
    init = gen(F, X0, t0, t0+(N-1)*h, h)
    return general_method(stepper, F, init.trajectory, t0, tf, h)


# Construct a combined predictor-corrector pair
def make_pc_stepper(predictor, corrector):
    def stepper(F, X, i, h):
        prediction = predictor(F, X, i, h)
        correction = corrector(F, X, i, h, prediction)
        return correction

    return stepper
