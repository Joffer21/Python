import matplotlib.pyplot as plt
import numpy as np

"""
Barras Matplotlib
Criando Barras
Com Pyplot, você pode usar a função bar() para desenhar gráficos de barras:
Exemplo:
Desenhe 4 barras:
"""

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()