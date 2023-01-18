#tres linhas para nosso compilador ser capaz de desenhar:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show

#Duas linhas para nosso compilador ser capas de desenhar:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()