import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('seaborn-dark')

data = np.random.rand(10,3)

fig, axes = plt.subplots(1,3, sharey=True)
plt.suptitle('2D Views')

ax1, ax2, ax3 = axes

ax1.scatter(data[:,0], data[:,1])
ax1.set_title('XY')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')

ax2.scatter(data[:,1], data[:,2])
ax2.set_title('YZ')
ax2.set_xlabel('Y')
ax2.set_ylabel('Z')

ax3.scatter(data[:,0], data[:,2])
ax3.set_title('XZ')
ax3.set_xlabel('X')
ax3.set_ylabel('Z')

plt.show()

    
