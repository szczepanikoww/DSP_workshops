import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# parameters
PERIOD_VECTOR_SIZE = 60
PERIOD_NUMBER = 5

# loading Rx vector from file and..
Rx = np.load('TxSignal_Exercise.npy')

# .. ploting it
plt.plot(Rx)
plt.grid()
plt.show()

# spliting vector into time slots coresponding to single periods
RxPeriods = np.reshape(Rx,(5,60))

# decoding amplitudes of Rx time slots

ampls = [] # create amplitude list
for RxPeriod in RxPeriods:
    t = np.linspace(0, 2*pi,PERIOD_VECTOR_SIZE, endpoint=False)
    Ref  = np.sin(t)     
    dot  = np.sum(Ref * RxPeriod)
    ampl = (2*dot)/PERIOD_VECTOR_SIZE 
    ampls.append(ampl)
    
print(ampls)  # print list
    



