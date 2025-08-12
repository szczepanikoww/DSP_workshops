import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

pi = np.pi

nums = [i * pi for i in range(1,6,2)]
steps = np.linspace(0,3*2*pi, 60, endpoint = False)
t = np.array([x for x in steps if x not in nums])

sin_a = (pi/2)*np.sin(t+pi)
trian_a = pi*signal.sawtooth(t,0.5)

sum_a = sin_a + trian_a

plt.plot(t,sin_a,'p', label='sinusoid', color='blue')
plt.plot(t, trian_a, '-p', label='triangle', color='green')
plt.plot(t,sum_a,'--',label='sum', color='red')

plt.title('trianle + sinus')
plt.xlabel('tempus[s]')
plt.ylabel('amplitudo[a.u.]')
plt.xlim(0,10)
plt.ylim(-4,6)
plt.axhline(y=0, color='orange')
plt.grid()
plt.legend()
plt.show()
