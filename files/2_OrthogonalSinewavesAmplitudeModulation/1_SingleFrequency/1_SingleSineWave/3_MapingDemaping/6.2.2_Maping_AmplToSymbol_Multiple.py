import numpy as np
import matplotlib.pyplot as plt
import mapper_lib as ml

for x in 2,4,8:

    symbols_l = np.array([])
    ampl_l = np.arange(-1.5,1.5,0.01)
    
    for ampl in ampl_l:
        symbol = ml.ampl_to_symbol(x, ampl)
        symbols_l = np.append(symbols_l, symbol)
    
    plt.plot(ampl_l,symbols_l,'-p', label=f'symbol nr = {x}') 

plt.legend()
plt.grid()
plt.xlabel('Symbol')
plt.ylabel('Amplitude')
plt.show()




