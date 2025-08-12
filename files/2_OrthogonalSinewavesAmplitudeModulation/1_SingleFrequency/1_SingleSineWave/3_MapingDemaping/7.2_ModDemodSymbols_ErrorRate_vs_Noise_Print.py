import numpy as np
from mapper_lib import symbol_to_ampl, ampl_to_symbol 

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000

NOISE_DEVIATIONS = [0.00 , 0.22, 0.44, 0.67, 0.89, 
                   1.11, 1.33, 1.56, 1.78, 2.00]
SYMBOL_NR = 8

t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, 
                endpoint=False)
Carrier = np.sin(t) 
Ref     = Carrier

print(f'SYMBOL_NR = {SYMBOL_NR}\n')
print('noise dev : error nr')
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
        
    
    NO_ERRORS = sum(symbols_rx != symbols_tx)
    print(f'{NOISE_DEVIATION} : {NO_ERRORS}')

