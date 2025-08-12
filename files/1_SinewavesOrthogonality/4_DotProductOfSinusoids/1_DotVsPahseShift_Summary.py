import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

phase_shift = np.linspace(0,pi,100)
dot_products = []

t = np.linspace(0,pi,30, endpoint=False)

for phase in phase_shift:
    ref = np.sin(t)
    shifted = np.sin(t + phase)
    
    ref_multi_shifted = ref * shifted
    dot_product = sum(ref_multi_shifted)
    dot_products.append(dot_product)


plt.plot(phase_shift, dot_products, color='blue')
plt.xlabel('shift')
plt.ylabel('dot')
plt.xlim(-0.2, 3.4)
plt.ylim(-16, 16)
plt.grid()
plt.title('dot product & phase shift')
plt.axhline(y=0, color='black')
plt.show()


