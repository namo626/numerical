import numpy as np


''' Single-steppers -------------------------------------------------------- '''

def euler_step(F, X, i, h):
    return X[i,:] + h*F(X[i,:])

def rk4_step(F, X, i, h):
    Xi = X[i, :]
    K1 = h * F(Xi)
    K2 = h * F(Xi + 0.5*K1)
    K3 = h * F(Xi + 0.5*K2)
    K4 = h * F(Xi + K3)
    return Xi + (1.0/6)*(K1 + 2*K2 + 2*K3 + K4)



''' Multi-steppers --------------------------------------------------------- '''

def adams_bashforth_4(F, X, i, h):
    K1 = 55 * F(X[i,:])
    K2 = -59 * F(X[i-1,:])
    K3 = 37 * F(X[i-2,:])
    K4 = -9 * F(X[i-3,:])
    return X[i,:] + (h/24)*(K1 + K2 + K3 + k4)


def adams_bashforth_5(F, X, i, h):
    A = X[i,:] + (h/720)*(1901 * F(X[i,:])
                          - 2774 * F(X[i-1,:])
                          + 2616 * F(X[i-2,:])
                          - 1274 * F(X[i-3,:])
                          + 251 * F(X[i-4,:]))
    return A


''' Corrector Methods (to be used with Predictor methods) ------------------- '''

def adams_moulton_4(F, X, i, h, prediction):
    K1 = 9 * prediction
    K2 = 19 * F(X[i,:])
    K3 = -5 * F(X[i-1,:])
    K4 = F([X,i-2,:])
    return X[i,:] + (h/24)*(K1 + K2 + K3 + K4)

def adams_moulton_5(F, X, i, h, prediction):
    return X[i,:] + (h/720)*(251 * F(prediction)
                             + 646 * F(X[i,:])
                             - 264 * F(X[i-1,:])
                             + 106 * F(X[i-2,:])
                             - 19 * F(X[i-3,:]))
