import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 100
AMPL_VECTOR = np.arange(0.5,4.5,0.5)
NOISE_DEVIATIONS = np.arange(0.05,1,0.05)

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t)

for j in range(0,len(NOISE_DEVIATIONS)):
    amplitudes_received = []
    for i in range(TIME_VECTOR_SIZE):
        amp = AMPL_VECTOR[i%8]
        
        # modulation
        Tx = amp * Carrier
        
        # channel
        Rx = Tx + np.random.normal(0,NOISE_DEVIATIONS[j],len(Tx))    
        
        # demodulation     
        dot  = np.dot(Carrier, Rx)
        ampl = (2*dot)/TIME_VECTOR_SIZE
        amplitudes_received.append(ampl)
        
    # PRESENTATION  
    # Rx plot
    plt.title('Estimation of acceptable noise dev.')
    plt.plot(amplitudes_received[0::8], 'p', color='red')           # each first
    plt.plot(amplitudes_received[1::8], 'p', color='orange')        # each second
    plt.plot(amplitudes_received[2::8], 'p', color='green')         # each third
    plt.plot(amplitudes_received[3::8], 'p', color='blue')          # each fourth
    plt.plot(amplitudes_received[4::8], 'p', color='black')         # each fifth
    plt.plot(amplitudes_received[5::8], 'p', color='purple')        # each sixth
    plt.plot(amplitudes_received[6::8], 'p', color='lightblue')     # each seventh
    plt.plot(amplitudes_received[7::8], 'p', color='yellow')        # each eigth
    plt.axhline(y=0,color='black')
    plt.yticks(np.arange(0, 5, 0.5))
    plt.grid(axis='y')
    plt.show()
    print(f'Noise Deviation: {NOISE_DEVIATIONS[j]:0.2f}')





