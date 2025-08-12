import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

Rx = np.load('TxSignal.npy')

plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid()
plt.show()

# PARAMETERS
TIME_VECTOR_SIZE = 60

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

ampl_sin_l = list()
ampl_cos_l = list()

for f in range(1,6):
    dot_sin = np.dot(np.sin(f*t),Rx)
    dot_cos = np.dot(np.cos(f*t), Rx)
    
    ampl_sin = 2 * dot_sin / TIME_VECTOR_SIZE
    ampl_cos = 2 * dot_cos / TIME_VECTOR_SIZE
    
    ampl_sin_l.append(ampl_sin) 
    ampl_cos_l.append(ampl_cos) 

for a in ampl_sin_l:
    print(f'{a:0.2f}',end=', ')    
print ()    
for a in ampl_cos_l:
    print(f'{a:0.2f}',end=', ')
    
    