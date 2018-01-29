import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('seaborn-poster')

r = np.random.randint(10000, 40000, 24)
theta = np.arange(1, 25) * np.pi / 24
xlabels = range(1,25)
xticks = np.arange(1, 25) * np.pi / 24

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)

ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_rlabel_position(-30)
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels)
plt.show()
