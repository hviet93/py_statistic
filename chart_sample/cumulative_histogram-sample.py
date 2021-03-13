import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)

fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.hist(data)
ax2.hist(data, cumulative=True)
plt.show()
