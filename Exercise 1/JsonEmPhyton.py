"""
JSON é uma sintaxe para armazenar e trocar dados.
JSON é texto, escrito com notação de objeto JavaScript.
O Python possui um pacote interno chamado json, que pode ser usado para trabalhar com dados JSON.
"""
import json

#Se você tiver uma string JSON, poderá analisá-la usando o método json.loads().
x = '{"name": "Joao", "age":"40", "city":"Lisboa"}' #Some JSON (Algum JSO)
y = json.loads(x) #Parse x (Analisar x)

print(y["name"]) #The result is a Python dictionary (O resultado é um dicionário Python)

#O resultado será um dicionário Python .

#--------------------------------------------------------------------------------------------------------
#Converter de Python para JSON
#Se você tiver um objeto Python, poderá convertê-lo em uma string JSON usando o método json.dumps().

#A Python object (dict) - (Um objeto Python (dict))
x = {
    "name": "Joao",
    "age": 40,
    "city": "Lisboa"
}

y = json.dumps(x) #Convert into JSON (converter em JSON)
print(y) #The result is a JSON string (o resultado é uma string JSON)

#---------------------------------------------------------------------------------------------------------

#Converter objetos Python em strings JSON e imprima os valores:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


#---------------------------------------------------------------------------------------------------------
#Converter um objeto Python contendo todos os tipos de dados legais:
x = {
  "name": "Joao",
  "age": 40,
  "married": True,
  "divorced": False,
  "children": ("Matheus","Murilo"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

#----------------------------------------------------------------------------------------------------------
"""
Formatar o resultado
O exemplos acima imprime uma string JSON, mas não é muito fácil de ler, sem recuos e quebras de linha.
O método json.dumps() possui parâmetros para facilitar a leitura do resultado:
Use o parâmetro indent para definir os números de recuos:
"""
x = {
  "name": "Joao",
  "age": 40,
  "married": True,
  "divorced": False,
  "children": ("Matheus","Murilo"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4)) #Use four indents to make it easier to read the result (Use quatro recuos para facilitar a leitura do resultado)
