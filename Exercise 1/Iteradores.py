"""
ITERADOR todos esses objetos possuem um método iter() que é usado para obter um iterador:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
"""

"""
Fazendo um loop através de um iterador
Também podemos usar um forloop para iterar por meio de um objeto iterável:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)
"""

"""
Criar um iterador
Para criar um objeto/classe como um iterador, você deve implementar os métodos __iter__() e __next__() para o seu objeto.
Como você aprendeu no capítulo Classes/Objetos do Python , todas as classes têm uma função chamada __init__(), que permite que você faça algumas inicializações quando o objeto está sendo criado.
O método ITER age de forma semelhante, você pode fazer operações (inicializar etc.), mas sempre deve retornar o próprio objeto iterador.
O método NEXT também permite fazer operações, devendo retornar o próximo item da sequência.


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
"""


"""
StopIteration
O exemplo acima continuaria indefinidamente se você tivesse instruções next() suficientes ou se fosse usado em um forloop.
Para evitar que a iteração continue para sempre, podemos usar a instrução StopIteration .
No método NEXT, podemos adicionar uma condição de finalização para gerar um erro se a iteração for feita um número especificado de vezes:
"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
