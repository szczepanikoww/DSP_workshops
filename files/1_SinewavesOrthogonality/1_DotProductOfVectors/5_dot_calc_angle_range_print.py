import numpy as np
from mylib import rotate_vector

green = [0,1];
blue = [0,1];


for k in range(0,361, 10):
    print(f'{k:03d}: {np.dot(green, blue) :+0.3f}')
    blue = rotate_vector(blue, 10)
    
    
    
    
    
    