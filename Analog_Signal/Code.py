import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 11)
x = (0.85) ** t
plt.figure(figsize=(10, 8))

#Signal

plt.subplot(2, 2, 1)
plt.title('Analog Signal', fontsize=20)
plt.plot(t, x, linewidth=3) 
plt.xlabel('t', fontsize=15)
plt.ylabel('amplitude', fontsize=15)
plt.legend(loc='upper right')  

plt.show()
