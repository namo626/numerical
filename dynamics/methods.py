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
