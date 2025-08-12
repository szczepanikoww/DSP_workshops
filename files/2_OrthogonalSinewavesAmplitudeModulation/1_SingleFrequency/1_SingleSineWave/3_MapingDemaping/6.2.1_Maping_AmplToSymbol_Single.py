import numpy as np
import matplotlib.pyplot as plt
import mapper_lib as ml

SYMBOL_NR = 8

symbols_l = np.array([])
ampl_l = np.arange(-1.5,1.5,0.01)

for ampl in ampl_l:
    symbol = ml.ampl_to_symbol(SYMBOL_NR, ampl)
    symbols_l = np.append(symbols_l, symbol)


plt.title(f'SYMBOL_NR = {SYMBOL_NR}')
plt.plot(ampl_l,symbols_l,'p')     
plt.grid()
plt.xlabel('Amplitude')
plt.ylabel('Symbol')



