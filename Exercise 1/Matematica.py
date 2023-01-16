"""
Matemática
O Python possui um conjunto de funções matemáticas integradas, incluindo um extenso módulo matemático,
que permite realizar tarefas matemáticas com números.
Funções matemáticas integradas
As funções min()e max() podem ser usadas para encontrar o valor mais baixo ou mais alto em um iterável:

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#---------------------------------------------------------------------------
#A função abs() retorna o valor absoluto (positivo) do número especificado:
x = abs(-7.25)
print(x)

#----------------------------------------------------------------------------
#A função pow() retorna o valor de x à potência de y (x ).
#Retorna  o valor de 4 à potência de 3 (o mesmo que 4 * 4 * 4):
x = pow(4, 3)
print(x)
"""

"""
O módulo de matemática
O Python também possui um módulo embutido chamado math, que estende a lista de funções matemáticas.
Para usá-lo, você deve importar o módulo math.
Depois de importar o módulo math , você pode começar a usar métodos e constantes do módulo.
O método math.sqrt() por exemplo, retorna a raiz quadrada de um número:
"""

import math

x = math.sqrt(64)
print(x)

#O método math.ceil() arredonda um número para cima até o inteiro mais próximo,
#O método math.floor() arredonda um número para baixo até o inteiro mais próximo e retorna o resultado:

x = math.ceil(1.4)
y = math.floor(1.4)
print(x)  #retorna 2
print(y)  #retorna 1

#A constante math.pi , retorna o valor de PI (3.14...):
x = math.pi
print(x)