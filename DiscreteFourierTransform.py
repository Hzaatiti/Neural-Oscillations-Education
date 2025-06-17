import matplotlib.pyplot as plt
import numpy as np

Fs = 2048;


f0 = 10

t = np.arange(0, 1,1/Fs) # 1 second
s = np.sin(2*np.pi*f0*t + 1.0) # sine wave with f0 frequency shifted by 1 second

plt.plot(t, s)
plt.show()
N = 2048
s[0:int(N/2)-1] = -1

plt.plot(t,s)
plt.show()


s = s + np.random.normal(0, 0.2, size = s.shape)  # Gaussian noise with 0 mean and 0.2 variance

N = 2048
baseCos = np.zeros((1+int(N/2),N))
baseSin = np.zeros((1+int(N/2),N))

print(baseCos)
print(baseSin)