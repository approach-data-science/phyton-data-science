import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

flg, ax = plt.subplots()
ax.plot(x,y)
plt.show()

