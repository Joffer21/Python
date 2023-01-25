import numpy
import matplotlib.pyplot as plt

"""
Aprendizado de Máquina
Distribuição normal de dados
No capítulo anterior aprendemos como criar um array completamente aleatório,
De um determinado tamanho, e entre dois valores dados.
Neste capítulo aprenderemos como criar um array onde os valores estão concentrados em torno de um determinado valor.
Na teoria da probabilidade, esse tipo de distribuição de dados é conhecido como distribuição normal de dados ou distribuição gaussiana de dados,
Em homenagem ao matemático Carl Friedrich Gauss, que criou a fórmula dessa distribuição de dados.
Exemplo:
Uma distribuição de dados normal típica:
"""

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()

"""
Nota: Um gráfico de distribuição normal também é conhecido como curva de sino por causa de sua forma característica de sino.

Histograma explicado
Usamos o array do numpy.random.normal() método, com 100.000 valores, para desenhar um histograma com 100 barras.
Especificamos que o valor médio é 5,0 e o desvio padrão é 1,0.
Significando que os valores devem estar concentrados em torno de 5,0, e raramente além de 1,0 da média.
E como você pode ver no histograma, a maioria dos valores está entre 4,0 e 6,0, com um máximo de aproximadamente 5,0.
"""