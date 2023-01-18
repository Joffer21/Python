"""
    Gravar em um arquivo existente
    Para gravar em um arquivo existente, você deve adicionar um parâmetro à função open():
    "a"- Anexar - será anexado ao final do arquivo
    "w"- Escrever - substituirá qualquer conteúdo existente
"""

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#Abra e leia o arquivo após o acréscimo:
f = open("demofile.txt", "r")
print(f.read())

#Abra o arquivo "demofile3.txt" e substitua o conteúdo:

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#Abra e leia o arquivo após a substituição:
f = open("demofile3.txt", "r")
print(f.read())

"""
    Criar um novo arquivo
    Para criar um novo arquivo em Python, utilize o open()método, com um dos seguintes parâmetros:
    "x"- Criar - criará um arquivo, retornará um erro se o arquivo existir
    "a"- Anexar - criará um arquivo se o arquivo especificado não existir
    "w"- Write - criará um arquivo se o arquivo especificado não existir
"""

#Exemplo: Crie um arquivo chamado "meuarquivo.txt":

f = open("myfile.txt", "x")

#Resultado: um novo arquivo vazio é criado!

#Exemplo: Crie um novo arquivo se ele não existir:

f = open("myfile.txt", "w")