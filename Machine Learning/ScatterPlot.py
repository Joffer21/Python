import numpy
import matplotlib.pyplot as plt

"""
Aprendizado de Máquina
Gráfico de Dispersão
Um gráfico de dispersão é um diagrama em que cada valor no conjunto de dados é representado por um ponto.
O módulo Matplotlib possui um método para desenhar gráficos de dispersão,
Ele precisa de duas matrizes do mesmo comprimento,
Uma para os valores do eixo x e outra para os valores do eixo y:

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

A matriz x representa a idade de cada carro.

A matriz y representa a velocidade de cada carro.

Exemplo
Use o método scatter() para desenhar um diagrama de gráfico de dispersão:
"""

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

"""
Gráfico de dispersão explicado
O eixo x representa as idades e o eixo y representa as velocidades.
O que podemos ler no diagrama é que os dois carros mais rápidos tinham ambos 2 anos
E o carro mais lento tinha 12 anos.
Nota: Parece que quanto mais novo o carro,
Mais rápido anda, mas pode ser coincidência, afinal registramos apenas 13 carros.
"""

#-----------------------------------------------------------------------------

"""
Distribuições de dados aleatórios
No Machine Learning, os conjuntos de dados podem conter milhares ou até milhões de valores.
Você pode não ter dados do mundo real ao testar um algoritmo,
Pode ser necessário usar valores gerados aleatoriamente.
Como aprendemos no capítulo anterior, o módulo NumPy pode nos ajudar com isso!
Vamos criar duas matrizes que são preenchidas com 1.000 números aleatórios de uma distribuição de dados normal.
A primeira matriz terá a média definida como 5,0 com um desvio padrão de 1,0.
A segunda matriz terá a média definida como 10,0 com um desvio padrão de 2,0:

Exemplo:
Um gráfico de dispersão com 1000 pontos:
"""

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()

"""
Gráfico de dispersão explicado
Podemos ver que os pontos estão concentrados em torno do valor 5 no eixo x e 10 no eixo y.
Também podemos ver que o spread é maior no eixo y do que no eixo x.
"""