import matplotlib.pyplot as plot
import seaborn as sb

edades=[12,15,13,12,18,20,19,20,13,12,13,17,15,16,13,14,13,17,19]

intervalos = range(min(edades), max(edades) + 2)
#intervalos=[10,13,16,19,22]

sb.histplot(edades, color='#F2AB6D', bins=intervalos, kde=True)

plot.title('Histograma de edades')
plot.xlabel('Edades')
plot.ylabel('Frecuencia')
plot.xticks(intervalos)
plot.show()