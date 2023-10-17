import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(2)
x = []
y = []
idx = []
for i in range(10):
    y.append(np.random.random())
    x.append(np.random.random())
    idx.append(i)
    ax[0].plot(idx, y, "bo-")
    ax[1].plot(idx, x, "ro-")
    plt.pause(1)
plt.show()