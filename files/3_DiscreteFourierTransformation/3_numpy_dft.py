import numpy as np
import matplotlib.pyplot as plt

def my_stem_plot(y,title,y_range=None):
    x = np.arange(len(y))    
    plt.stem(x,y,'-b', markerfmt='sb')

    plt.xticks(x)
    
    if y_range:
        plt.ylim(y_range)
        plt.yticks(np.arange(*y_range))
    
    plt.grid()
    plt.title(title)
    fig = plt.gcf()
    fig.set_size_inches(4, 3.6)
    plt.show()

SAMPLE_NR = 10
FREQ = 3

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)

samples =  np.cos(3*t) + 0.2 * np.sin(t)
 
my_stem_plot(samples,f'samples',y_range=(-6,7))

fft = np.fft.fft(samples)
my_stem_plot(fft.real, 'real',y_range=(-6,7))
my_stem_plot(fft.imag, 'imag',y_range=(-6,7))

