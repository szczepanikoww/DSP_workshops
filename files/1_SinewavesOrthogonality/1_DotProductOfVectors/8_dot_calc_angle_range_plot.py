import numpy as np
from mylib import rotate_vector
import matplotlib.pyplot as plt

green = [0, 1]
v = [0, 1]

angle_list = list()
dot_list = list()

for angle in range(0,361,10):    
    angle_list.append(angle)    
    v = rotate_vector(v,10)
    dot = np.dot(green,v)
    dot_list.append(dot)

plt.plot(angle_list,dot_list)

plt.xlabel('angle')
plt.ylabel('dot')

plt.grid()



