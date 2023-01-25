import numpy


"""
Aprendizado de Máquina - Modo Mediano Médio
Média, Mediana e Moda
O que podemos aprender olhando para um grupo de números?

No Machine Learning (e na matemática) geralmente existem três valores que nos interessam:

Média - O valor médio
Mediana - O valor do ponto médio
Moda - O valor mais comum
Exemplo: Registramos a velocidade de 13 carros:

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

Qual é a média, o meio ou o valor de velocidade mais comum?

Significar
O valor médio é o valor médio.

Para calcular a média, encontre a soma de todos os valores e divida a soma pelo número de valores:

(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77

O módulo NumPy tem um método para isso.
Aprenda sobre o módulo NumPy em nosso Tutorial NumPy .

Exemplo:
Use o método NumPy mean()para encontrar a velocidade média:
"""

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)

#---------------------------------------------------------------------------

"""
Mediana
O valor mediano é o valor no meio, depois de ter classificado todos os valores:

77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111

É importante que os números sejam classificados antes que você possa encontrar a mediana.
O módulo NumPy tem um método para isso:

Exemplo:
Use o método NumPy median()para encontrar o valor do meio:
"""

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)

"""
Se houver dois números no meio, divida a soma desses números por dois.

77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103

(86 + 87) / 2 = 86.5
"""

#------------------------------------------------------------------------------

"""
Modo
O valor Mode é o valor que aparece mais vezes:

99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86

O módulo SciPy possui um método para isso. Aprenda sobre o módulo SciPy em nosso Tutorial SciPy .

Exemplo
Use o método SciPy mode()para encontrar o número que mais aparece:

from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)
"""