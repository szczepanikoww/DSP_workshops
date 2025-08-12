import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

def myDFT(samples):
    N = len(samples)
    real = list()
    image = list()
    
    for f in range(N):
        angles = 2 * np.pi * f * np.arange(N) / N
        real.append(np.dot(samples, np.cos(angles)))
        image.append(np.dot(samples, np.sin(angles)))

    return real, image

# loads samples from .wav file with exemplary DTFM signal
# adapt file path 
samples = read(r'wav\a.wav')
samplig_freq = samples[0]
samples = samples[1]
samples = samples[:1024]

samples = np.array(samples, float)
samples = samples - np.mean(samples)

plt.plot(samples)

real, imag = myDFT(samples)

freq = np.linspace(0, samplig_freq, len(samples), endpoint=False)

real = np.array(real, float)
imag = np.array(imag, float)

amplitude = np.sqrt(real**2 + imag**2)

plt.figure()
plt.plot(freq, amplitude)
plt.grid()
plt.title("Amplitudy sinusoid")

plt.figure()
plt.plot(freq, real,label='real')
plt.plot(freq, imag,label='imag')
plt.grid()
plt.legend()
plt.title("Amplitudy składowych sin i cos")

#culd be usefool for zooming
#plt.xlim(-10,10)
#plt.ylim(-20_000,20_000)


# use commenst to swith between myDTF and numpy DTF (FFT)
#fft = np.fft.fft(samples)
#real = fft.real
#imag = fft.imag



























'''
real = np.array(real)
imag = np.array(imag)

magnitude = np.sqrt(real**2 + imag**2)
plt.figure()
plt.plot(magnitude, label='Magnitude')
plt.grid()
plt.legend()
plt.show()
print(np.argsort(magnitude)[-2:])

freq_real = np.array(real) * (samplig_freq/len(samples))
freq_imag = np.array(imag) * (samplig_freq/len(samples))
'''





