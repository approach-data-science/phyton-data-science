import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors

monedas = [20, 10, 25, 30]
nombres = ["Ana", "Juan", "Diana", "Catalina"]

normdata=colors.Normalize(min(monedas), max(monedas))
colormap=plt.get_cmap("Greens")
colores= colormap(normdata(monedas))

desfase=(0, 0, 0, 0.1)
plt.pie(monedas, labels=nombres, autopct="%0.1f %%", colors=colores, explode=desfase)
plt.axis("equal")
plt.show()
