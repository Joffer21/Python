import numpy
import matplotlib.pyplot as plt

"""
Aprendizado de Máquina
Regressão Polinomial
Se seus pontos de dados claramente não se ajustarem a uma regressão linear (uma linha reta através de todos os pontos de dados),
Pode ser ideal para regressão polinomial.

A regressão polinomial, como a regressão linear,
Usa a relação entre as variáveis ​​x e y para encontrar a melhor maneira de traçar uma linha através dos pontos de dados.
Como funciona?
Python tem métodos para encontrar uma relação entre pontos de dados e para desenhar uma linha de regressão polinomial.
Mostraremos como usar esses métodos em vez de passar pela fórmula matemática.
No exemplo abaixo, cadastramos 18 carros passando por um determinado posto de pedágio.
Registramos a velocidade do carro e a hora do dia (hora) em que ocorreu a passagem.
O eixo x representa as horas do dia e o eixo y representa a velocidade:

Exemplo
Comece desenhando um gráfico de dispersão:
"""

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

plt.scatter(x, y)
plt.show()

#----------------------------------------------------------------------------

#Exemplo
#Linha de Regressão Polinomial:

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

"""
Exemplo explicado
Importe os módulos que você precisa.
Crie as matrizes que representam os valores dos eixos x e y:

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

NumPy tem um método que nos permite fazer um modelo polinomial:
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

Em seguida, especifique como a linha será exibida, começamos na posição 1 e terminamos na posição 22:
myline = numpy.linspace(1, 22, 100)

Desenhe o gráfico de dispersão original:
plt.scatter(x, y)

Desenhe a linha de regressão polinomial:
plt.plot(myline, mymodel(myline))

Mostre o diagrama:
plt.show()
"""

#-------------------------------------------------------------------------------------------------------------

"""
R ao quadrado
É importante saber quão bem é a relação entre os valores dos eixos x e y,
Se não houver relação, a regressão polinomial não pode ser usada para prever nada.
A relação é medida com um valor chamado r-quadrado.
O valor de r ao quadrado varia de 0 a 1, onde 0 significa nenhuma relação e 1 significa 100% relacionado.
O Python e o módulo Sklearn calcularão esse valor para você, tudo o que você precisa fazer é alimentá-lo com os arrays x e y:

Exemplo
Quão bem meus dados se encaixam em uma regressão polinomial?
"""