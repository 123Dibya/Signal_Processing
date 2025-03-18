import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 5                # Amplitude
f = 50               # Frequency in Hz
fs = 1000         # Sampling frequency (higher than Nyquist)

# Time array
t = np.linspace(0, 0.1, fs)  # 0.1 seconds, 1000 samples

# Signals
sine_wave = a * np.sin(2 * np.pi * f * t)


# Plotting
plt.figure(figsize=(12, 8))

# Sine Signal
plt.subplot(2, 2, 1)
plt.plot(t, sine_wave, linewidth=3, label='Sine wave', color='blue')
plt.xlabel("Time (s)", fontsize=10)
plt.ylabel("Amplitude", fontsize=10)
plt.title('Sine Signal', fontsize=20)
plt.legend(fontsize=10, loc='upper right')

plt.show()
