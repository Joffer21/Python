"""
    Python RegEx
    Um RegEx, ou Expressão Regular, é uma sequência de caracteres que forma um padrão de pesquisa.
    RegEx pode ser usado para verificar se uma string contém o padrão de pesquisa especificado.
    Python tem um pacote interno chamado re, que pode ser usado para trabalhar com Expressões Regulares.
    Importe o módulo re
"""

import re

#Depois de importar o remódulo, você pode começar a usar expressões regulares:
#Pesquise a string para ver se ela começa com "The" e termina com "Spain":

txt = "The rain in Spain"  #A chuva na Espanha
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

"""
    O módulo re oferece um conjunto de funções que nos permite pesquisar uma string em busca de uma correspondência:

    findall - Retorna uma lista contendo todas as correspondências
    search - Retorna um objeto Match se houver uma correspondência em qualquer lugar da string
    split - Retorna uma lista onde a string foi dividida em cada correspondência
    sub - Substitui uma ou mais correspondências por uma string
"""

#A função findall()
#Retorna uma lista contendo todas as correspondências.
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#--------------------------------------------------------------------------------------------------

#A lista contém as correspondências na ordem em que foram encontradas.
#Se nenhuma correspondência for encontrada, uma lista vazia será retornada:

txt = "The rain in Spain"

#Check if "Portugal" is in the string (Verifique se "Portugal" está na string:)
x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#----------------------------------------------------------------------------------------------------

#A função search()
#Pesquisa a string em busca de uma correspondência e retorna um objeto Match se houver uma correspondência.
#Se houver mais de uma correspondência, apenas a primeira ocorrência da correspondência será retornada:

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#Se nenhuma correspondência for encontrada, o valor Noneé retornado:

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

#------------------------------------------------------------------------------------------------------

#A função split()
#Retorna uma lista onde a string foi dividida em cada correspondência:
#Dividir em cada caractere de espaço em branco:

x = re.split("\s", txt)
print(x)

#Você pode controlar o número de ocorrências especificando o parâmetro maxsplit

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#-------------------------------------------------------------------------------------------------------

#A função sub()
#Substitui as correspondências pelo texto de sua escolha:
#Exemplo: Substitua todos os caracteres de espaço em branco pelo número 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#Você pode controlar o número de substituições especificando o parâmetro count:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#--------------------------------------------------------------------------------------------------------

#Objeto correspondente
#Um Match Object é um objeto que contém informações sobre a pesquisa e o resultado.
#Observação: Caso não haja correspondência, Noneserá retornado o valor, no lugar do Objeto de correspondência.

#Exemplo: Faça uma pesquisa que retornará um Match Object:

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #Isso imprimirá um objeto

"""
    O objeto Match possui propriedades e métodos usados ​​para recuperar informações sobre a pesquisa e o resultado:
    .span()retorna uma tupla contendo as posições inicial e final da correspondência.
    .string retorna a string passada para a função
    .group()retorna a parte da string onde houve uma correspondência
"""

#Exemplo
#Imprima a posição (posição inicial e final) da primeira ocorrência de correspondência.
#A expressão regular procura todas as palavras que começam com "S" maiúsculo:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#Imprima a string passada para a função:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

#Imprima a parte da string onde houve uma correspondência.
#A expressão regular procura todas as palavras que começam com "S" maiúsculo:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

#Observação: Caso não haja correspondência, Noneserá retornado o valor, no lugar do Objeto de correspondência.
