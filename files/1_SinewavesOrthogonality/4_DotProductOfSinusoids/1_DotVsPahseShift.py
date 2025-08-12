import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETER
PHASE_SHIFT = pi

# VECTORS
t = np.linspace(0, 2*pi,30, endpoint=False)

Ref = np.sin(t)
Shifted = np.sin(t + PHASE_SHIFT)
Ref_mult_Shifted = Ref * Shifted
dot_product = np.sum(Ref_mult_Shifted)

# PLOTS (HINT: use separate plots, not one with grid)

# components
plt.plot(t,Ref,'-p', label='Ref', color='blue')
plt.plot(t,Shifted, '-p', label='Shifted', color='green')

plt.grid()
plt.legend()
plt.title('Components')
plt.xlim(-0.5, 6.5)
plt.ylim(-1.1,1.1)
plt.axhline(y=0, color='black')
plt.show()

# multiplication, HINT: use "stem" function for ploting
plt.stem(t,Ref_mult_Shifted, linefmt='blue', markerfmt='orange',
         bottom=0, label='Ref_mult_shifted')
plt.xlim(-0.5,6.5)
plt.ylim(-1.1,1.1)
plt.title( 'Multiplication')
plt.grid()
plt.legend()
plt.show()

# print phase shift and dot product value
print('Phase Shift = ', round(PHASE_SHIFT,2))
print('Dot product = ', round(dot_product,2))

