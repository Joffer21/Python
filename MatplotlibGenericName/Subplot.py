import matplotlib.pyplot as plt
import numpy as np

"""
Subtrama do Matplotlib
Exibir Múltiplos Gráficos
Com a função subplot(), você pode desenhar vários gráficos em uma figura:
"""

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 15, 35])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()

#---------------------------------------------------------------------------------

"""
A função subplot() recebe três argumentos que descrevem o layout da figura.
O layout é organizado em linhas e colunas, que são representadas pelo primeiro e segundo argumento.
O terceiro argumento representa o índice do gráfico atual.

plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.
#A figura tem 1 linha, 2 colunas, e este plot é o primeiro plot.

plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.
#A figura tem 1 linha, 2 colunas, e este gráfico é o segundo gráfico.

Então, se quisermos uma figura com 2 linhas e 1 coluna
(o que significa que os dois gráficos serão exibidos um em cima do outro em vez de lado a lado), podemos escrever a sintaxe assim:

Exemplo: Desenhe 2 parcelas uma sobre a outra:
"""

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()

#Você pode desenhar quantos gráficos quiser em uma figura, apenas descreva o número de linhas, colunas e o índice do gráfico.
#Exemplo: Desenhe 6 parcelas:

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()

#------------------------------------------------------------------------------------------------

"""
Título
Você pode adicionar um título a cada gráfico com a função title():
Exemplo: 2 lotes, com títulos:
"""

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.show()

#-------------------------------------------------------------------------------

"""
Super Título
Você pode adicionar um título à figura inteira com a função suptitle():
Exemplo:Adicione um título para a figura inteira:
"""

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()