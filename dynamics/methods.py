import importlib
import lineFlow
import steppers
importlib.reload(lineFlow)
importlib.reload(steppers)
from lineFlow import *
from steppers import *

''' A collection of common methods '''

def euler(F, X0, t0, tf, h):
    return singlestep_method(euler_step, F, X0, t0, tf, h)

def rk2(F, X0, t0, tf, h):
    return singlestep_method(rk2_step, F, X0, t0, tf, h)

def rk4(F, X0, t0, tf, h):
    return singlestep_method(rk4_step, F, X0, t0, tf, h)

def adams_bashforth_moulton2(F, X0, t0, tf, h):
    stepper = make_pc_stepper(adams_bashforth_2, adams_moulton_2)
    return multistep_method(2, rk4, stepper, F, X0, t0, tf, h)

def adams_bashforth_moulton4(F, X0, t0, tf, h):
    stepper = make_pc_stepper(adams_bashforth_4, adams_moulton_4)
    return multistep_method(4, rk4, stepper, F, X0, t0, tf, h)

def adams_bashforth_moulton5(F, X0, t0, tf, h):
    stepper = make_pc_stepper(adams_bashforth_5, adams_moulton_5)
    return multistep_method(5, rk4, stepper, F, X0, t0, tf, h)


def rkf4(F, init, steps, h0, delta):
    dim = init.size
    X = np.zeros((steps+1, dim))
    t = np.zeros((steps+1,))
    e = np.zeros((steps+1,))

    K = np.zeros((6,dim))
    a = np.array([16/135, 0, 6656/12825, 28561/56430, -9/50, 2/55])
    b = np.array([1/360, 0, -128/4275, -2197/75240, 1/50, 2/55])

    X[0,:] = init
    h = h0
    for i in range(steps):
        K[0,:] = h * F(X[i,:])
        K[1,:] = h * F(X[i,:] + K[0,:]*(1/4))
        K[2,:] = h * F(X[i,:] + K[0,:]*(3/32) + K[1,:]*(9/32))
        K[3,:] = h * F(X[i,:] + K[0,:]*(1932/2197) - K[1,:]*(7200/2197) + K[2,:]*(7296/2197))
        K[4,:] = h * F(X[i,:] + K[0,:]*(439/216) - K[1,:]*8 + K[2,:]*(3680/513) - K[3,:]*(845/4104))
        K[5,:] = h * F(X[i,:] + K[0,:]*(-8/27) + K[1,:]*2 + K[2,:]*(-3544/2565) + K[3,:]*(1859/4104) - K[4,:]*(11/40))

        X[i+1,:] = X[i,:] + np.dot(a, K)
        e[i+1]   = np.dot(b, K)
        t[i+1]   = t[i] + h

        # Adjust the step size
        h = 0.9 * h * (delta/np.abs(e[i+1,:]))**(1/1+5)

    return Solution(t, X, h[1], dim)
