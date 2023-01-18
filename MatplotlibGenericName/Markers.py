import matplotlib.pyplot as plt
import numpy as np

"""
Marcadores
Você pode usar o argumento de palavra-chave marker para enfatizar cada ponto com um marcador especificado:
"""
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

"""
Strings de formato fmt
Você também pode usar o parâmetro de notação de string de atalho para especificar o marcador.
Este parâmetro também é chamado fmt, e é escrito com esta sintaxe:
marker|line|color
"""
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()

"""
Tamanho do marcador
Você pode usar o argumento de palavra-chave markersize ou a versão mais curta ms para definir o tamanho dos marcadores:
"""
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

"""
Cor do marcador
Você pode usar o argumento de palavra-chave "markeredgecolor" ou o mais curto "mec" para definir a cor da borda dos marcadores:
Exemplo: Defina a cor EDGE para vermelho:
"""

ypoints = np.array([1, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

#Você pode usar o argumento de palavra-chave "markerfacecolor" ou o mais curto "mfc" para definir a cor dentro da borda dos marcadores:

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '*', ms = 20, mfc = 'g')
plt.show()

#Use os argumentos "mec" e para colorir todo o marcador:"mfc"

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()

"""
Você também pode usar valores de cores hexadecimais:

plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')

Ou qualquer um dos 140 nomes de cores suportados .

Exemplo
Marque cada ponto com a cor chamada "hotpink":

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
"""


