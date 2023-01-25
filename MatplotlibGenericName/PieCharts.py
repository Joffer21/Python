import matplotlib.pyplot as plt
import numpy as np

"""
Criando Gráficos de Pizza
Com Pyplot, você pode usar a função pie() para desenhar gráficos de pizza:
Exemplo:
Um gráfico de pizza simples:
"""

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 

"""
Como você pode ver, o gráfico de pizza desenha uma peça (chamada de cunha)
Para cada valor na matriz (neste caso [35, 25, 25, 15]).
Por padrão, a plotagem da primeira cunha começa no eixo x e se move no sentido anti-horário:
Nota: O tamanho de cada cunha é determinado comparando o valor com todos os outros valores, usando esta fórmula:
O valor dividido pela soma de todos os valores: x/sum(x)
"""

#-------------------------------------------------------------------------------------------------------------------------

"""
Etiquetas
Adicione rótulos ao gráfico de pizza com o parâmetro label.
O parâmetro label deve ser uma matriz com um rótulo para cada fatia:
Exemplo:
Um gráfico de pizza simples:
"""

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()

#---------------------------------------------------------------------------------------------------------------

"""
Ângulo inicial
Conforme mencionado, o ângulo inicial padrão está no eixo x, mas você pode alterar o ângulo inicial especificando um parâmetro startangle.
O parâmetro startangle é definido com um ângulo em graus, o ângulo padrão é 0:
"""

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

#----------------------------------------------------------------------------------------------------

"""
Explodir
Talvez você queira que uma das cunhas se destaque?
O parâmetro explode permite que você faça isso.
O parâmetro explode, se especificado, e não None, deve ser um array com um valor para cada fatia.
Cada valor representa a que distância do centro cada fatia é exibida:
Exemplo:
Puxe a fatia "Maçãs" 0,2 do centro da torta:
"""

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()

#-----------------------------------------------------------------------------

"""
Sombra
Adicione uma sombra ao gráfico de pizza definindo o parâmetro shadows como True:
Exemplo:
Adicione uma sombra:
"""

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()

#---------------------------------------------------------------------------

"""
cores
Você pode definir a cor de cada fatia com o parâmetro colors.
O parâmetro colors, se especificado, deve ser um array com um valor para cada fatia:
Exemplo:
Especifique uma nova cor para cada fatia:
"""

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

#--------------------------------------------------------------------------------------

"""
Lenda
Para adicionar uma lista de explicação para cada fatia, use a função legend():
Exemplo:
Adicione uma legenda:
"""

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()

#-----------------------------------------------------------------------------------

"""
Legenda Com Cabeçalho
Para adicionar um cabeçalho à legenda, adicione o parâmetro title à função legend .
Exemplo:
Adicione uma legenda com um cabeçalho:
"""

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 