import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({'España': [826, 943, 942, 901],
                    'Colombia': [668, 781, 791, 813],
                    'Mexico': [488, 553, 563, 537]},
                    index=('Lunes', 'Martes', 'Miercoles', 'Jueves'))
total = data.sum(axis=1)


plt.bar(data.index, data.España + data.Colombia + data.Mexico, label='España')
plt.bar(data.index, data.Colombia + data.Mexico, label='Colombia')
plt.bar(data.index, data.Mexico, label='Mexico')

plt.legend(loc='best')

plt.show()
