import numpy as np
import matplotlib.pyplot as plt
from mylib import myDFT, my_stem_plot

SAMPLE_NR = 10
SIN_FREQ = 3 

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)

samples =  np.cos(t*1) * 2/5 + np.sin(t*4) * 4/5
my_stem_plot(samples,'samples')

real, imag = myDFT(samples)

my_stem_plot(real, 'myDFT real', y_range=(-6,7))
my_stem_plot(imag, 'myDFT imag', y_range=(-6,7))

fft = np.fft.fft(samples)
my_stem_plot(fft.real, 'FFt real', y_range=(-6,7))
my_stem_plot(fft.imag, 'FFt imag', y_range=(-6,7))





