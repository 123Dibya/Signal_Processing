import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 1000  # Sampling frequency
t = np.arange(0, 1, 1/fs)  # Time vector

# Original sine wave signal
sg = np.sin(2 * np.pi * 5 * t)  # 5 Hz sine wave
plt.subplot(2, 2, 1)
plt.plot(t, sg)
plt.title("Original Sine Wave Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Add Gaussian noise
noise = np.random.normal(0, 0.5, sg.shape)
noisy_signal = sg + noise
plt.subplot(2, 2, 2)
plt.plot(t, noisy_signal)
plt.title("Noisy Sine Wave Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Low-pass Butterworth filter (4th order, 10 Hz cutoff)
cutoff_frequency = 10  
b, a = signal.butter(4, cutoff_frequency / (0.5 * fs), btype="low") #0rder,Cut-pff.type=low
filtered_signal = signal.filtfilt(b, a, noisy_signal)

# Plot the filtered signal
plt.subplot(2, 2, 3)
plt.plot(t, filtered_signal, label="Filtered Signal", color="red")
plt.plot(t, noisy_signal, label="Noisy Signal", color="gray", alpha=0.5)
plt.title("Filtered Sine Wave Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()
