import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# parameters
PERIOD_VECTOR_SIZE = 60

# loading Rx vector from file and..
Rx = np.load('TxSignal.npy')

# .. ploting it
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid()
plt.show()

# CALLCULATION
t = np.linspace(0, 2*pi,PERIOD_VECTOR_SIZE, endpoint=False)

# references
ref_f1_sin = np.sin(t)
ref_f1_cos = np.cos(t)

ref_f2_sin = np.sin(2*t)
ref_f2_cos = np.cos(2*t)

# dot products
dot_f1_sin = np.dot(ref_f1_sin, Rx) 
dot_f1_cos = np.dot(ref_f1_cos, Rx) 

dot_f2_sin = np.dot(ref_f2_sin, Rx)
dot_f2_cos = np.dot(ref_f2_cos, Rx)

# amplitudes
amp_f1_sin = 2*dot_f1_sin/PERIOD_VECTOR_SIZE  
amp_f1_cos = 2*dot_f1_cos/PERIOD_VECTOR_SIZE 

amp_f2_sin = 2*dot_f2_sin/PERIOD_VECTOR_SIZE
amp_f2_cos = 2*dot_f2_cos/PERIOD_VECTOR_SIZE

# PRESENTATION
print(f'amp_f1_sin={amp_f1_sin:0.1f}')
print(f'amp_f1_cos={amp_f1_cos:0.1f}')
print(f'amp_f2_sin={amp_f2_sin:0.1f}')
print(f'amp_f2_cos={amp_f2_cos:0.1f}')

