import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(20, size=10) + 1j * np.random.randint(20, size=10)

plt.scatter(a.real, a.imag)

plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid()

plt.savefig('imaginary_plot.png')
plt.show()
