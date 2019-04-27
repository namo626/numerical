import importlib
import lineFlow
import solution
importlib.reload(solution)
importlib.reload(lineFlow)
from solution import *
from lineFlow import *
from functools import partial


''' Harmonic Oscillator '''
def spring_eq(k, m, state):
    x = state[0]
    y = state[1]
    return np.array([y, (-k/m)*x])

F_spring = partial(spring_eq, 1, 1)
X0_spring = np.array([3, 0])
# spring_rk4 = rk4_system(F_spring, X0_spring, 0, 30, 0.1)
# spring_euler = euler_system(F_spring, X0_spring, 0, 30, 0.1)

''' Lorenz System '''
def lorenz_eq(sigma, rho, beta, state):
    x = state[0]; y = state[1]; z = state[2]
    return np.array([sigma*(y-x),
                     x*(rho-z) - y,
                     x*y - beta*z])

F_lorenz = partial(lorenz_eq, 10, 28, 8/3)
X0_lorenz = np.array([1.0, 1.0, 1.0])

# lorenz_rk4 = rk4_system(F_lorenz, X0_lorenz, 0, 40, 0.01)
lorenz_rk4_test = rk4(F_lorenz, X0_lorenz, 0, 40, 0.01)
# lorenz_euler = euler_system(F_lorenz, X0_lorenz, 0, 40, 0.01)
lorenz_euler_test = euler(F_lorenz, X0_lorenz, 0, 40, 0.01)
lorenz_pc = adams_pc(F_lorenz, X0_lorenz, 0, 40, 0.01)
lorenz_pc_new = adams_bashforth_moulton(F_lorenz, X0_lorenz, 0, 40, 0.01)




def func(t, x):
    return (t*x - math.pow(x, 2)) / math.pow(t, 2)

def sol(t):
    return (t / (0.5 + math.log(t)))

x1 = RK4(func, 2.0, 1.0, 3.0, 1/128)
x2 = RK4(func, 2.0, 1.0, 3.0, 1/256)
