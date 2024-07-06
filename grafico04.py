import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.DataFrame({'España': [826, 943, 942, 901],
                    'Colombia': [668, 781, 791, 813],
                    'Mexico': [488, 553, 563, 537]},
                    index=('Lunes', 'Martes', 'Miercoles', 'Jueves'))

n = len(data.index)
x = np.arange(n)
width=0.25

plt.bar(x - width, data.España, width=width, label='España')
plt.bar(x, data.Colombia, width=width, label='Colombia')
plt.bar(x + width, data.Mexico, width=width, label='Mexico')

plt.xticks(x, data.index)
plt.legend(loc='best')

plt.show()
