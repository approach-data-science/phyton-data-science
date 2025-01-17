import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = x*2

plt.plot(x, y)

x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]

plt.plot(x, y1, '-.')

plt.xlabel("eje X")
plt.ylabel("eje Y")
plt.title("Titulo del grafico")

plt.fill_between(x, y, y1, color='green', alpha=0.5)
plt.show()