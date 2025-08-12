import numpy as np

green = np.array([0.000,0.050,0.000,-0.050,0.000,0.050,0.000,-0.050,0.000,0.050,0.000])
blue  = np.array([0.088,0.088,0.088,0.442,0.530,0.000,-0.530,-0.442,-0.088,-0.088,-0.088])

dot_product = np.sum(green*blue)
print(round(dot_product,6))


ziel = [0.000,0.050,0.000,-0.050,0.000,0.050,0.000,-0.050,0.000,0.050,0.000]
nieb = [0.088,0.088,0.088,0.442,0.530,0.000,-0.530,-0.442,-0.088,-0.088,-0.088]
wynik = 0
for i in range(0,len(ziel)):
    wynik = wynik + ziel[i]*nieb[i]
print(wynik)
