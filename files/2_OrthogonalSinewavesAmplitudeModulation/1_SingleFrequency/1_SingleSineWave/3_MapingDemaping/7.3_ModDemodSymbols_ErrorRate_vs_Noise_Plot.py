import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol 

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000

NOISE_DEVIATIONS = np.linspace(0,5,20)
SYMBOLS = [2,4,8]

t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, 
                endpoint=False)
Carrier = np.sin(t) 
Ref     = Carrier

for SYMBOL_NR in SYMBOLS:
    errors = np.array([])
    for NOISE_DEVIATION in NOISE_DEVIATIONS:
        # TRANSMISION-RECEPTION
        symbols_tx = np.random.randint(0,SYMBOL_NR,TRANSMISIONS_NR)    
        symbols_rx = list()
        for symbol in symbols_tx:        
            # modulation
            ampl = symbol_to_ampl(SYMBOL_NR, symbol)
            Tx = ampl*Carrier        
            # real channel
            Rx = Tx + np.random.normal(0, NOISE_DEVIATION, len(Tx))   
            # demodulation
            ampl = (np.dot(Rx,Ref)/TIME_VECTOR_SIZE)*2  
            symbol = ampl_to_symbol(SYMBOL_NR, ampl)
            symbols_rx = np.append(symbols_rx, symbol)
            
        no_errors = sum(symbols_rx != symbols_tx)
        errors = np.append(errors, no_errors)
        
    plt.plot(NOISE_DEVIATIONS, errors, '-p', label = f'symbol nr = {SYMBOL_NR}')

plt.xlabel('noise deviation')
plt.ylabel('error nr')
plt.grid()
plt.legend()
plt.show()


