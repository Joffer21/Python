import matplotlib.pyplot as plt
from scipy import stats

"""
Aprendizado de Máquina - Regressão Linear
Regressão
O termo regressão é usado quando você tenta encontrar a relação entre as variáveis.
No Machine Learning e na modelagem estatística,
Essa relação é usada para prever o resultado de eventos futuros.

Regressão linear
A regressão linear usa a relação entre os pontos de dados para traçar uma linha reta através de todos eles.
Esta linha pode ser usada para prever valores futuros.
No Machine Learning, prever o futuro é muito importante.

Como funciona?
Python tem métodos para encontrar uma relação entre pontos de dados
E para desenhar uma linha de regressão linear.
Mostraremos como usar esses métodos em vez de passar pela fórmula matemática.
No exemplo abaixo, o eixo x representa a idade e o eixo y representa a velocidade.
Registramos a idade e a velocidade de 13 carros ao passarem por um pedágio.
Vamos ver se os dados que coletamos podem ser usados ​​em uma regressão linear:

Exemplo:
Comece desenhando um gráfico de dispersão:
"""

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

#---------------------------------------------------------------------------------------

#Exemplo
#Importe scipye desenhe a linha de Regressão Linear:

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

"""
Exemplo explicado
Importe os módulos que você precisa.

Você pode aprender sobre o módulo Matplotlib em nosso Tutorial Matplotlib .

Você pode aprender sobre o módulo SciPy em nosso Tutorial SciPy .

import matplotlib.pyplot as plt
from scipy import stats

Crie as matrizes que representam os valores dos eixos x e y:

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

Execute um método que retorne alguns valores-chave importantes da Regressão Linear:
 --> slope, intercept, r, p, std_err = stats.linregress(x, y)

Crie uma função que usa os valores slopee interceptpara retornar um novo valor.
Este novo valor representa onde no eixo y o valor x correspondente será colocado:
 --> def myfunc(x):
  return slope * x + intercept

Execute cada valor da matriz x por meio da função.
Isso resultará em uma nova matriz com novos valores para o eixo y:
 --> mymodel = list(map(myfunc, x))

Desenhe o gráfico de dispersão original: --> plt.scatter(x, y)

Desenhe a linha de regressão linear: --> plt.plot(x, mymodel)

Mostre o diagrama: --> plt.show()
"""

#---------------------------------------------------------------------------

"""
R para Relacionamento
É importante saber como é a relação entre os valores do eixo x e os valores do eixo y,
Se não houver relação a regressão linear não pode ser usada para prever nada.
Essa relação - o coeficiente de correlação - é chamada r.
O valor r varia de -1 a 1, onde 0 significa nenhum relacionamento e 1 (e -1) significa 100% relacionado.
O Python e o módulo Scipy calcula esse valor para você,
Tudo o que precisa fazer é alimentá-lo com os valores x e y.
Exemplo:
Quão bem meus dados se ajustam em uma regressão linear?
"""

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)

#Nota: O resultado -0,76 mostra que existe uma relação, não perfeita,
# Mas indica que poderíamos usar a regressão linear em previsões futuras.

#---------------------------------------------------------------------------------

"""
Prever Valores Futuros
Agora podemos usar as informações que reunimos para prever valores futuros.

Exemplo: Vamos tentar prever a velocidade de um carro de 10 anos.

Para fazer isso, precisamos da mesma função myfunc() do exemplo acima:

def myfunc(x):
  return slope * x + intercept

Exemplo
Preveja a velocidade de um carro de 10 anos:
"""

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)

print(speed)

#O exemplo previu uma velocidade de 85,6, que também podemos ler no diagrama:

"""
Ajuste ruim?
Vamos criar um exemplo onde a regressão linear não seria o melhor método,
Para prever valores futuros.

Exemplo:
Esses valores para os eixos x e y devem resultar em um ajuste muito ruim para a regressão linear:
"""

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

#E o relacionamento r?

#Exemplo:
#Você deve obter um valor muito baixo r.

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)

#O resultado: 0,013 indica uma relação muito ruim e nos diz que esse conjunto de dados,
# Não é adequado para regressão linear.