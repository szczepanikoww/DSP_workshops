import numpy as np
from mapper_lib import symbol_to_ampl, ampl_to_symbol 

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 10

NOISE_DEVIATION = 2.0
SYMBOL_NR = 4

t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, endpoint=False)
carrier_sin = ref_sin = np.sin(t) 
carrier_cos = ref_cos = np.cos(t) 

# TRANSMISION-RECEPTION
symbols_tx_sin = np.random.randint(0,SYMBOL_NR,TRANSMISIONS_NR)  
symbols_tx_cos = np.random.randint(0,SYMBOL_NR,TRANSMISIONS_NR)  

symbols_rx_sin = list()
symbols_rx_cos = list()

for symbol_sin, symbol_cos in zip(symbols_tx_sin,symbols_tx_cos):        
    # modulation
    ampl_sin = symbol_to_ampl(SYMBOL_NR, symbol_sin)
    ampl_cos = symbol_to_ampl(SYMBOL_NR, symbol_cos)
    Tx = ampl_sin * carrier_sin + ampl_cos * carrier_cos     
    # real channel
    Rx = Tx + np.random.normal(loc=0, scale=NOISE_DEVIATION, size=len(Tx))    
    # demodulation
    ampl_sin = 2 * np.dot(ref_sin,Rx) / TIME_VECTOR_SIZE        
    ampl_cos = 2 * np.dot(ref_cos,Rx) / TIME_VECTOR_SIZE
    
    symbol_sin = ampl_to_symbol(SYMBOL_NR, ampl_sin)
    symbol_cos = ampl_to_symbol(SYMBOL_NR, ampl_cos)
    
    symbols_rx_sin.append(symbol_sin)
    symbols_rx_cos.append(symbol_cos)

# PRESENTATION   
symbols_rx_sin = np.array(symbols_rx_sin) # list to numpy array
symbols_rx_cos = np.array(symbols_rx_cos)

print('SIN')
print('symbols_rx:', symbols_tx_sin)
errors = symbols_rx_sin != symbols_tx_sin
print('match:', ~errors)
print('errors nr:', sum(errors))

print('COS')  
print('symbols_rx:', symbols_tx_cos)
errors = symbols_rx_cos != symbols_tx_cos
print('match:', ~errors)
print('errors nr:', sum(errors))



