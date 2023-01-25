import sys
import matplotlib

import matplotlib.pyplot as plt
import numpy as np

"""
Histograma
Um histograma é um gráfico que mostra as distribuições de frequência .
É um gráfico que mostra o número de observações dentro de cada intervalo dado.
Exemplo: digamos que você pergunte a altura de 250 pessoas, você pode acabar com um histograma como este:

Criar Histograma
No Matplotlib, usamos a hist()função para criar histogramas.
A função hist() usará uma matriz de números para criar um histograma, a matriz é enviada para a função como um argumento.
Para simplificar usamos o NumPy para gerar aleatoriamente um array com 250 valores, onde os valores vão se concentrar em torno de 170, e o desvio padrão é 10.
Exemplo:
Uma distribuição de dados normal por NumPy:


x = np.random.normal(170, 10, 250)

print(x)
"""

#----------------------------------------------------------------------------------------------

"""
A função hist() lerá a matriz e produzirá um histograma:
Exemplo:
Um histograma simples:
"""

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()