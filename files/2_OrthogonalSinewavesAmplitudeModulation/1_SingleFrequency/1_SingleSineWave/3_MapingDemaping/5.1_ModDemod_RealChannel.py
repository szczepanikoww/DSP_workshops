import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2)

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
amplitudes_received = []
Carrier = np.sin(t)

for amp in AMPL_VECTOR:
    
    # modulation
    Tx = amp * Carrier
    
    # channel
    Rx = Tx + np.random.normal(0,0.3,len(Tx))    
    
    # demodulation     
    dot  = np.dot(Carrier, Rx)
    ampl = (2*dot)/TIME_VECTOR_SIZE
    amplitudes_received.append(ampl)
    
amplitudes_received = np.array(amplitudes_received)
errors = np.round(amplitudes_received - AMPL_VECTOR,8)

# PRESENTATION  
# Rx plot
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()

print(f'received amplitudes: {amplitudes_received}')
print(f'errors: {errors}')


