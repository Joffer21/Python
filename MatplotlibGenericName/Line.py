import matplotlib.pyplot as plt
import numpy as np

"""
Linha Matplotlib
Estilo de linha
Você pode usar o argumento de palavra-chave linestyle, ou mais curto ls, para alterar o estilo da linha plotada:
"""

ypoints = np.array([3, 8, 1, 10])

#plt.plot(ypoints, linestyle = 'dotted')
plt.plot(ypoints, linestyle = 'dashed')  #Use uma linha tracejada:
plt.show()

#---------------------------------------------------------------------------------------------------------------------------

"""
Sintaxe mais curta
O estilo de linha pode ser escrito em uma sintaxe mais curta:
linestylepode ser escrito como ls.
dotted pode ser escrito como ":"
dashed pode ser escrito como "--"

Exemplo: Sintaxe mais curta:
plt.plot(ypoints, ls = ':')
"""

#--------------------------------------------------------------------------------------------------------------

"""
Cor da linha
Você pode usar o argumento de palavra-chave "color" ou o mais curto "c" para definir a cor da linha:
"""

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()

"""
Você também pode usar valores de cores hexadecimais:
Exemplo: Plote com uma bela linha verde:

plt.plot(ypoints, c = '#4CAF50')
"""
#------------------------------------------------------------------------------------------------------------------

"""
Espessura da linha
Você pode usar o argumento de palavra-chave "linewidth" ou o mais curto "lw" para alterar a largura da linha.
O valor é um número flutuante, em pontos:
Exemplo: Plote com uma linha de 20,5pt de largura:
"""

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '10.5')
plt.show()

#-------------------------------------------------------------------------------------------------------------------------

"""
Múltiplas Linhas
Você pode plotar quantas linhas quiser simplesmente adicionando mais funções plt.plot():
Exemplo: Desenhe duas linhas especificando uma função plt.plot() para cada linha:
"""

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

"""
Você também pode plotar muitas linhas adicionando os pontos dos eixos x e y para cada linha na mesma função plt.plot().
(Nos exemplos acima, especificamos apenas os pontos no eixo y, o que significa que os pontos no eixo x obtiveram os valores padrão (0, 1, 2, 3).)
Os valores x e y vêm em pares:
Exemplo: Desenhe duas linhas especificando os valores dos pontos x e y para ambas as linhas:
"""

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

