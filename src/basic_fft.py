#!user/bin/env python3

import numpy as np
from scipy import signal
from scipy.fft import fft, fftfreq
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Number of sample points
N = 600
# Sample spacing
Fs = 8000.0e6  # Sampling frequency in Hz
Ts = 1.0 / Fs
#print(Ts)

x = np.linspace(0.0, N*Ts, N, endpoint=False)
f = np.arange(-Fs/2, Fs/2, Fs/N)
# Create a signal with two frequencies
y = np.exp(1j*500.0e6 * 2.0*np.pi*x) + 0.5*np.exp(1j*800.0e6 * 2.0*np.pi*x)
win = signal.windows.flattop(N)
y_win = y * win
plt.figure(1)
plt.plot(np.real(y_win))
plt.grid()

# Compute the FFT
yf = fft(y_win)
yf_shift = np.fft.fftshift(yf) * 1.0/N * 1/(sum(win)/ N)
yf_shift_dB = 10*np.log10(np.abs(yf_shift))
# Get the frequency bins
#xf = fftfreq(N, Ts)[:N//2]
#xf = fftfreq(N, Ts)[0:N]

plt.figure(2)
plt.plot(f, yf_shift_dB[0:N])
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT of the signal')
plt.show()
plt.close('all')
