import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 11)
x = (0.85) ** t
plt.figure(figsize=(10, 8))

#Sampling

plt.subplot(2, 2, 2)
plt.title('Sampling', fontsize=20)
plt.plot(t, x, linewidth=3)
n = t

markerline, stemlines, baseline = plt.stem(n, x)
plt.setp(stemlines,color='b', linewidth= 3)
plt.setp(markerline,color='r', markersize= 6)
plt.setp(baseline,color='g',linewidth=3)
plt.xlabel('n' , fontsize = 15)
plt.ylabel('amplitude', fontsize = 15)
plt.legend(loc='upper right')

plt.show()
