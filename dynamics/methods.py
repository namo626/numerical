import importlib
import lineFlow
import steppers
importlib.reload(lineFlow)
importlib.reload(steppers)
from lineFlow import *
from steppers import *

''' A collection of common methods '''

def adams_bashforth_moulton(F, X0, t0, tf, h):
    stepper = make_pc_stepper(adams_bashforth, adams_moulton)
    return multistep_method(5, stepper, F, X0, t0, tf, h)

def euler(F, X0, t0, tf, h):
    return singlestep_method(euler_step, F, X0, t0, tf, h)

def rk4(F, X0, t0, tf, h):
    return singlestep_method(rk4_step, F, X0, t0, tf, h)
