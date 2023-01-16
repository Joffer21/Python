"""
HERANÇA
Nos permite definir uma classe que herda todos os métodos e propriedades de outra classe.
A classe (PERSON) pai é a classe da qual está sendo herdada, também chamada de classe base.
Classe filha (STUDENT) é a classe que herda de outra classe, também chamada de classe derivada.
"""

class Person:                               #Classe pai
    def __init__(self, fname, lname):
        self.firstname = fname              #Propriedades da classe
        self.lastname = lname               #Propriedades da classe

    def printname(self):                    #Método da classe
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Joao", "Ferreira")
x.printname()

class Student(Person):                       #Classe Filho
    def __init__(self, fname, lname, year):  #Propriedades da classe Filho
        super().__init__(fname, lname)       #Propriedades da classe Pai herdada
        self.graduationyear = year           #Propriedades da classe Filho

    def welcome(self):                       #Método da classe Filho
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Matheus", "Ferreira", 2023)
x.welcome()