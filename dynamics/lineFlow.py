import numpy as np
import math
import matplotlib.pyplot as plt
import importlib
import solution
importlib.reload(solution)
from solution import *


def single_step_method(updater, F, X0, t0, tf, h):
    t       = np.arange(t0, tf+h, h)
    steps   = t.shape[0] - 1
    X       = np.zeros((steps+1, X0.shape[0]))
    X[0, :] = X0

    for i in range(steps):
        X[i+1, :] = updater(X[i, :])

    return Solution(t, X, 'single-step', h, X0.shape[0])

def euler(F, X0, t0, tf, h):
    def g(Xt):
        return Xt + h*F(Xt)

    return single_step_method(g, F, X0, t0, tf, h)

def rk4(F, X0, t0, tf, h):
    def runge_kutta(Xt):
        K1 = h * F(Xt)
        K2 = h * F(Xt + 0.5*K1)
        K3 = h * F(Xt + 0.5*K2)
        K4 = h * F(Xt + K3)
        return Xt + (1.0/6)*(K1 + 2*K2 + 2*K3 + K4)

    return single_step_method(runge_kutta, F, X0, t0, tf, h)


''' Predictor Methods '''

def adams_bashforth(i, X, F, h):
    A = X[i,:] + (h/720)*(1901 * F(X[i,:])
                          - 2774 * F(X[i-1,:])
                          + 2616 * F(X[i-2,:])
                          - 1274 * F(X[i-3,:])
                          + 251 * F(X[i-4,:]))
    return A



''' Corrector Methods (Technically Implicit) '''

def adams_moulton(i, X, F, h, pred):
    return X[i,:] + (h/720)*(251 * F(pred)
                             + 646 * F(X[i,:])
                             - 264 * F(X[i-1,:])
                             + 106 * F(X[i-2,:])
                             - 19 * F(X[i-3,:]))


''' General Predictor-Corrector method '''
def predictor_corrector(predictor, corrector, N, F, X0, t0, tf, h):
    t     = np.arange(t0, tf+h, h)
    steps = t.shape[0] - 1
    X     = np.zeros((steps+1, X0.shape[0]))

    # generate N initial values for the multistep predictor, X(t0) to X(t0 + (N-1)h)
    # using RK4
    init      = rk4(F, X0, t0, t0+(N-1)*h, h)
    X[0:N, :] = init.trajectory[0:N, :]

    for i in range(N-1, steps):
        pred = predictor(i, X, F, h)
        X[i+1,:] = corrector(i, X, F, h, pred)

    return Solution(t, X, 'Predictor-Corrector', h, X0.shape[0])


''' Predictor-Corrector using Adams-Bashforth-Moulton '''
def adams_pc(F, X0, t0, tf, h):
    return predictor_corrector(adams_bashforth, adams_moulton, 5, F, X0, t0, tf, h)
