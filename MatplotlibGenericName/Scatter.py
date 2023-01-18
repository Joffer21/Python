import matplotlib.pyplot as plt
import numpy as np

"""
Matplotlib Dispersão
Criando Gráficos de Dispersão
Com o Pyplot, você pode usar a função scatter() para desenhar um gráfico de dispersão.
A função scatter() plota um ponto para cada observação. Ele precisa de duas matrizes do mesmo comprimento, uma para os valores do eixo x e outra para valores no eixo y:
Exemplo: Um gráfico de dispersão simples:
"""

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

"""
A observação do exemplo acima é resultado da passagem de 13 carros.
O eixo X mostra a idade do carro.
O eixo Y mostra a velocidade do carro quando ele passa.
Há alguma relação entre as observações?
Parece que quanto mais novo o carro, mais rápido ele anda, mas pode ser coincidência, afinal registramos apenas 13 carros.
"""

#-----------------------------------------------------------------------------------------------------------------

"""
Comparar parcelas
No exemplo acima, parece haver uma relação entre velocidade e idade, mas e se plotarmos as observações de outro dia também? O gráfico de dispersão nos dirá algo mais?
Exemplo: Desenhe dois gráficos na mesma figura:
"""

#Day one, the age and speed of 13 cars:
#Dia um, a idade e a velocidade de 13 carros:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#Day two, the age and speed of 15 cars:
#Dia dois, a idade e a velocidade de 13 carros:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()

#Nota: Os dois gráficos são plotados com duas cores diferentes, por padrão azul e laranja, você aprenderá como alterar as cores mais adiante neste capítulo.
#Ao comparar os dois gráficos, acho que é seguro dizer que ambos nos levam à mesma conclusão: quanto mais novo o carro, mais rápido ele dirige.

#-----------------------------------------------------------------------------------------------------------------------------

"""
Cores
Você pode definir sua própria cor para cada gráfico de dispersão com o "color" ou o argumento "c":
Exemplo: Defina sua própria cor dos marcadores:
"""

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()

#------------------------------------------------------------------------------

"""
Pinte cada ponto
Você pode até definir uma cor específica para cada ponto usando uma matriz de cores como valor para o argumento "c":
Nota: Você não pode usar o argumento "color" para isso, apenas o argumento "c".
"""

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()

#----------------------------------------------------------------------------------------------------

"""
Mapa de Cores
O módulo Matplotlib possui vários mapas de cores disponíveis.
Um mapa de cores é como uma lista de cores, onde cada cor tem um valor que varia de 0 a 100.
Este mapa de cores é chamado de 'viridis' e, como você pode ver, varia de 0, que é a cor roxa, até 100, que é a cor amarela.

Como usar o ColorMap
Você pode especificar o mapa de cores com o argumento de palavra-chave cmapcom o valor do mapa de cores, neste caso, 'viridis'que é um dos mapas de cores integrados disponíveis no Matplotlib.
Além disso, você deve criar uma matriz com valores (de 0 a 100), um valor para cada ponto no gráfico de dispersão:
Exemplo: Crie uma matriz de cores e especifique um mapa de cores no gráfico de dispersão:
"""

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()

#---------------------------------------------------------------------------------------------

#Você pode incluir o mapa de cores no desenho incluindo a declaração plt.colorbar():

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()

#-------------------------------------------------------------------------------------------------

"""
Tamanho
Você pode alterar o tamanho dos pontos com o argumento "s".
Assim como as cores, certifique-se de que a matriz de tamanhos tenha o mesmo comprimento que as matrizes dos eixos x e y:
Exemplo: Defina seu próprio tamanho para os marcadores:
"""

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()

#----------------------------------------------------------------------------

"""
Alfa
Você pode ajustar a transparência dos pontos com o argumento "alpha".
Assim como as cores, certifique-se de que a matriz de tamanhos tenha o mesmo comprimento que as matrizes dos eixos x e y:
Exemplo: Defina seu próprio tamanho para os marcadores:
"""

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()

#---------------------------------------------------------------------------------------------------------------------------------

"""
Combinar tamanho de cor e alfa
Você pode combinar um mapa de cores com diferentes tamanhos de pontos.
Isso é melhor visualizado se os pontos forem transparentes:
Exemplo:
Crie matrizes aleatórias com 100 valores para pontos x, pontos y, cores e tamanhos:
"""

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()