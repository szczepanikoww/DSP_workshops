import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 100
AMPL_VECTOR = (1, 2, 3, 4)
NOISE_DEVIATION = 1

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
amplitudes_received = []
Carrier = np.sin(t)

for i in range(TIME_VECTOR_SIZE):
    amp = AMPL_VECTOR[i%4]
    
    # modulation
    Tx = amp * Carrier
    
    # channel
    Rx = Tx + np.random.normal(0,NOISE_DEVIATION,len(Tx))    
    
    # demodulation     
    dot  = np.dot(Carrier, Rx)
    ampl = (2*dot)/TIME_VECTOR_SIZE
    amplitudes_received.append(ampl)
    
# PRESENTATION  
# Rx plot
plt.plot(amplitudes_received[0::4], 'p', color='red')       # each first
plt.plot(amplitudes_received[1::4], 'p', color='orange')    # each second
plt.plot(amplitudes_received[2::4], 'p', color='green')     # each third
plt.plot(amplitudes_received[3::4], 'p', color='blue')      # each fourth
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()







