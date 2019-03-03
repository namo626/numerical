import numpy as np
from numpy import fft
import matplotlib.pyplot as plt

N = 200
xs = np.linspace(0, 2*np.pi, N)
ys1 = np.sin(3*xs)**2
ys2 = np.cos(2*xs)**3 + np.cos(np.sqrt(2)*xs)

F1 = fft.fft(ys1) / N
F2 = fft.fft(ys2) / N
spectrum1 = np.abs(F1)

# frequency / cofficient index
js = np.arange(0,N,1)

# reconstructing the function at a single point
def fourier_series(coeffs, n, x):
    g = 0
    for i in range(-n, n+1):
        gn = coeffs[np.abs(i)] * np.exp(1j * i * x)
        g = g + gn

    return g

# approximating the function at given points xs
# n is the summation limit
def fourier_vector(coeffs, n, xs):
    return np.real(np.array([fourier_series(coeffs, n, x) for x in xs]))

approx1_5 = fourier_vector(F1, 5, xs)
approx1_6 = fourier_vector(F1, 6, xs)

approx2_5 = fourier_vector(F2, 5, xs)
approx2_6 = fourier_vector(F2, 6, xs)

# plotting
plt.figure()
plt.plot(xs, ys1, xs, approx1_5)
plt.figure()
plt.plot(xs, ys2, xs, approx2_5)
plt.show()
