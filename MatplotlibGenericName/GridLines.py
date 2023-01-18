import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib Adicionando Linhas de Grade
Adicionar linhas de grade a um gráfico
Com o Pyplot, você pode usar a função grid() para adicionar linhas de grade ao gráfico.
Exemplo: Adicione linhas de grade ao gráfico:
"""

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()

#-----------------------------------------------------------------------------------------

"""
Especifique quais linhas de grade exibir
Você pode usar o parâmetro "axis na função grid() para especificar quais linhas de grade exibir.
Os valores legais são: 'x', 'y' e 'ambos'. O valor padrão é 'ambos'.
Exemplo: Exibir apenas linhas de grade para o eixo x:
"""

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x') #vertical
#plt.grid(axis = 'y')  #horizontal

plt.show()

#------------------------------------------------------------------------------------------------------

"""
Você também pode definir as propriedades de linha da grade,
Assim: grid(color = ' color ', linestyle = ' linestyle ', linewidth = number ).
Exemplo: Defina as propriedades da linha da grade:
"""

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()