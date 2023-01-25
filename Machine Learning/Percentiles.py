import numpy

"""
Aprendizado de Máquina - Percentis
O que são percentis?
Os percentis são usados ​​em estatísticas para fornecer um número que descreve o valor ao qual uma determinada porcentagem dos valores é inferior.

Exemplo: Digamos que temos um array das idades de todas as pessoas que moram em uma rua.

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

Qual é o percentil 75.? A resposta é 43, o que significa que 75% das pessoas têm 43 anos ou menos.
O módulo NumPy possui um método para encontrar o percentil especificado:

Exemplo:
Use o método NumPy percentile()para encontrar os percentis:
"""

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

#x = numpy.percentile(ages, 75)
x = numpy.percentile(ages, 90)  #Qual é a idade em que 90% das pessoas são mais jovens?


print(x)