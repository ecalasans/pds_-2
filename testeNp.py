import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 30000)
markerline, stemlines, baseline = plt.stem(x, np.sin(x), '-.')
plt.setp(baseline, color='r', linewidth=2)
plt.show()