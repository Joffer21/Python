"""
Escopo
Uma variável só está disponível dentro da região em que é criada. Isso é chamado de escopo .
Escopo Local: uma variável criada dentro de uma função pertence ao escopo local dessa função e só pode ser usada dentro dessa função.
"""
def myfunc():
    x = 300
    def myinnerfunc(): #A variável x não está disponível fora da função, mas está disponível para qualquer função dentro da função.
        print(x)
    myinnerfunc()

myfunc()