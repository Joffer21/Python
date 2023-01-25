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

#-------------------------------------------------------------------------------------------

"""
A função bar() recebe argumentos que descrevem o layout das barras.

As categorias e seus valores representados pelo primeiro e segundo argumento como matrizes.

Exemplo:
x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)
"""

#------------------------------------------------------------------------------------------

"""
Barras horizontais
Se você quiser que as barras sejam exibidas horizontalmente em vez de verticalmente, use a função barh():
Exemplo:
Desenhe 4 barras horizontais:
"""

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

#---------------------------------------------------------------------------------

"""
Cor da Barra
O bar() e barh() pegue o argumento de palavra-chave "color" para definir a cor das barras:
Exemplo:
Desenhe 4 barras vermelhas:
"""

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()

#-----------------------------------------------------------------------------------------------

"""
Largura da barra
O bar() leva o argumento de palavra-chave width para definir a largura das barras:
Exemplo:
Desenhe 4 barras muito finas:
"""

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()

#O valor de largura padrão é 0,8

#---------------------------------------------------------------------------------------

"""
Altura da barra
O barh() leva o argumento de palavra-chave height para definir a altura das barras:
Exemplo:
Desenhe 4 barras muito finas:
"""

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.show()

#O valor de altura padrão é 0,8

#----------------------------------------------------------------------------------------------

