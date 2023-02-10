import numpy as np
import timeit
def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

def FFT(x):
    """A recursive implementation of the 1D Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
 
    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized
        return DFT_slow(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:N / 2] * X_odd,
                               X_even + factor[N / 2:] * X_odd])

def test():
    x = np.random.random(1024)
    np.allclose(DFT_slow(x), np.fft.fft(x))

timer1=timeit.Timer("DFT_slow(x)",setup="from __main__ import DFT_slow")
print("%DFT(x) timeit ",timer1.timeit(number=1)) 

print("%np.fft.fft(x) timeit " ,timeit.Timer("np.fft.fft(x)",setup="import numpy as np").timeit(number=1)) 