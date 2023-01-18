import numpy as np
import matplotlib.pyplot as plt

"""
Rótulos e Título do Matplotlib
Criar rótulos para um gráfico
Com o Pyplot, você pode usar as funções xlabel() e ylabel() para definir um rótulo para os eixos x e y.
Exemplo: Adicione rótulos aos eixos x e y:
"""

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")  #Pulso médio
plt.ylabel("Calorie Burnage")  #Queima de Calorias

plt.show()

#--------------------------------------------------------------------------------------------------------

"""
Criar um título para um enredo
Com o Pyplot, você pode usar a função title() para definir um título para o gráfico.
Exemplo: Adicione um título de gráfico e rótulos para os eixos x e y:
"""

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data") #Dados do Relógio Esportivo
plt.xlabel("Average Pulse")    #Pulso médio
plt.ylabel("Calorie Burnage")  #Queima de Calorias

plt.show()

#--------------------------------------------------------------------------------------------------------

"""
Definir propriedades de fonte para títulos e rótulos
Você pode usar o parâmetro "fontdict" em xlabel(), ylabel() e title() para definir as propriedades da fonte para o título e os rótulos.
Exemplo: Defina as propriedades da fonte para o título e os rótulos:
"""

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
font3 = {'family':'serif','color':'green','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font3)

plt.plot(x, y)
plt.show()

#--------------------------------------------------------------------------------------------------------------

"""
Posicione o Título
Você pode usar o parâmetro "loc" in title() para posicionar o título.
Os valores legais são: 'esquerda(left)', 'direita(right)' e 'centro'. O valor padrão é 'center'.
Exemplo: Posicione o título à esquerda:
"""

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()

