"""
    A manipulação de arquivos é uma parte importante de qualquer aplicativo da web.
    Python tem várias funções para criar, ler, atualizar e deletar arquivos.
    A função chave para trabalhar com arquivos em Python é a open()função.
    A open()função recebe dois parâmetros; nome do arquivo e modo .
    Existem quatro métodos diferentes (modos) para abrir um arquivo:

    "r"- Leitura - Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existir
    "a"- Anexar - Abre um arquivo para anexar, cria o arquivo se ele não existir
    "w"- Write - Abre um arquivo para escrita, cria o arquivo se ele não existir
    "x"- Criar - Cria o arquivo especificado, retorna um erro se o arquivo existir

    Além disso, você pode especificar se o arquivo deve ser tratado como modo binário ou texto

    "t"- Texto - Valor padrão. modo de texto
    "b"- Binário - modo binário (por exemplo, imagens)


f = open("demofile.txt")

#O código acima é o mesmo que:

f = open("demofile.txt", "rt")

#Nota: Certifique-se de que o arquivo existe, caso contrário, você receberá um erro.
"""

#Para abrir o arquivo, use a função open() interna.
#A função open() retorna um objeto de arquivo, que possui um método read() para ler o conteúdo do arquivo:

f = open("demofile.txt", "r")
print(f.read())

#Por padrão, o método read() retorna o texto inteiro, mas você também pode especificar quantos caracteres deseja retornar:

f = open("demofile.txt", "r")
print(f.read(5))

#Você pode retornar uma linha usando o readline()método:
#Exemplo: Leia uma linha do arquivo:

f = open("demofile.txt", "r")
print(f.readline())

#Chamando readline() duas vezes, você pode ler as duas primeiras linhas:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

#Ao percorrer as linhas do arquivo, você pode ler o arquivo inteiro, linha por linha:

#Exemplo: Percorra o arquivo linha por linha:

f = open("demofile.txt", "r")
for x in f:
  print(x)

#É uma boa prática sempre fechar o arquivo quando terminar de usá-lo.

#Exemplo: Feche o arquivo quando terminar:

f = open("demofile.txt", "r")
print(f.readline())
f.close()

#Você deve sempre fechar seus arquivos, em alguns casos, devido ao buffer, as alterações feitas em um arquivo podem não aparecer até que você feche o arquivo.