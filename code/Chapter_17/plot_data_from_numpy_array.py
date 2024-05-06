from matplotlib import pyplot as plt
import numpy as np

# array = np.arange(1, 6)
data = np.arange(1, 21).reshape(5, 4)

plt.plot(data.transpose())
plt.show()
