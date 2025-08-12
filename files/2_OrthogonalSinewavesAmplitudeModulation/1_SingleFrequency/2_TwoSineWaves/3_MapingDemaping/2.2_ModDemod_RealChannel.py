import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60

AMPL_VECTOR_SIN = ( 0.12, -3.4, 5.6, -7.8)
AMPL_VECTOR_COS = ( 8.7,   6.5, 4.3,  2.1)

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

carrier_sin = ref_sin = np.sin(t) 
carrier_cos = ref_cos = np.cos(t) 

amplitudes_sin = list()
amplitudes_cos = list()

for ampl_sin, ampl_cos in zip(AMPL_VECTOR_SIN, AMPL_VECTOR_COS):
    
    # modulation
    Tx = (ampl_sin*carrier_sin) + (ampl_cos*carrier_cos)     
    
    # real channel
    Rx = Tx + np.random.normal(0,2,len(Tx))
        
    # demodulation
    ampl = (np.dot(Rx,ref_sin)/TIME_VECTOR_SIZE)*2  
    amplitudes_sin.append(ampl)
    
    ampl = (np.dot(Rx,ref_cos)/TIME_VECTOR_SIZE)*2  
    amplitudes_cos.append(ampl)

# PRESENTATION  
# Rx plot
plt.plot(Rx)
plt.axhline(y=0, color='black')
plt.grid()
plt.show()

# amplitudes
amplitudes_sin = np.array(amplitudes_sin) # convert list to numpy 1D array
amplitudes_cos = np.array(amplitudes_cos) # ...
np.set_printoptions(precision=2)          # set numpy array print precision

print(f'amplitudes_sin = {amplitudes_sin}')
errors_sin = amplitudes_sin - AMPL_VECTOR_SIN
print(f'errors_sin = {errors_sin}')
print(f'amplitudes_cos = {amplitudes_cos}')
errors_cos = amplitudes_cos - AMPL_VECTOR_COS
print(f'errors_cos = {errors_cos}')


