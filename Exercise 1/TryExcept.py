"""
    Quando ocorre um erro, ou exceção, como chamamos, o Python normalmente para e gera uma mensagem de erro.
    O bloco try  permite que você teste um bloco de código em busca de erros.
    O bloco except  permite lidar com o erro.
    O bloco else  permite executar o código quando não há erro.
    O bloco finally  permite que você execute o código, independentemente do resultado dos blocos try e except.
"""

#O bloco try irá gerar uma exceção, pois x não está definido:

try:
  print(x)
except:
  print("An exception occurred")  
  
#resposta: Ocorreu uma exceção

#Como o bloco try gera um erro, o bloco except será executado.
#Sem o bloco try, o programa falhará e gerará um erro:

#-----------------------------------------------------------------------------------------------------------------

#Você pode definir quantos blocos de exceção quiser, por exemplo, se quiser executar um bloco de código especial para um tipo especial de erro:
#Exemplo: Imprima uma mensagem se o bloco try gerar um NameError e outra para outros erros:

try:
  print(x)
except NameError:
  print("Variable x is not defined")  #A variável x não está definida
except:
  print("Something else went wrong")  #Algo mais deu errado

#-----------------------------------------------------------------------------------------------------------------

#Você pode usar a else para definir um bloco de código a ser executado se nenhum erro for gerado:
#Neste exemplo, o bloco try não gera nenhum erro:

try:
  print("Hello")
except:
  print("Something went wrong")  
else:
  print("Nothing went wrong")   
  
#Algo deu errado
#Nada deu

#------------------------------------------------------------------------------------------------------------------

#O bloco finally, se especificado, será executado independentemente se o bloco try gerar um erro ou não.

try:
  print(x)
except:
  print("Something went wrong")  
finally:
  print("The 'try except' is finished")  

#Algo deu errado
#O 'try except' está terminado
#Isso pode ser útil para fechar objetos e limpar recursos:
#Tente abrir e gravar em um arquivo que não é gravável:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")  #Algo deu errado ao gravar no arquivo
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  #Algo deu errado ao abrir o arquivo

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Levantar uma exceção como desenvolvedor Python, você pode optar por lançar uma exceção se ocorrer uma condição.
#Para lançar (ou gerar) uma exceção, use a palavra-chave raise.
#Exemplo: Gere um erro e pare o programa se x for menor que 0:

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")  
  
#Desculpe, não há números abaixo de zero

#A palavra-chave raise é usada para gerar uma exceção.
#Você pode definir que tipo de erro gerar e o texto a ser impresso para o usuário.

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")  #Somente números inteiros são permitidos

