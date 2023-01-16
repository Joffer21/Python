"""
Datas uma data em Python não é um tipo de dados próprio,
mas podemos importar um módulo nomeado datetime para trabalhar com datas como objetos de data.
"""
import datetime

#Módulo datetime e exiba a data atual:
#A data contém ano, mês, dia, hora, minuto, segundo e microssegundo.
#x = datetime.datetime.now()
#print(x)

#Retorne o ano e o nome do dia da semana:
#x = datetime.datetime.now()
#print(x.year)
#print(x.strftime("%A"))

"""
Criando objetos de Data:
Para criar uma data, podemos usar a DATATIME classe (construtor) do módulo datetime .
A classe datetime() requer três parâmetros para criar uma data: ano, mês, dia.

x = datetime.datetime(2023, 1, 16)
print(x)
"""


"""
O método strftime()
O datetime objeto tem um método para formatar objetos de data em strings legíveis.
O método é chamado strftime() e recebe um parâmetro, format, para especificar o formato da string retornada.
"""
x = datetime.datetime(2023, 1, 16)
print(x.strftime("%B"))