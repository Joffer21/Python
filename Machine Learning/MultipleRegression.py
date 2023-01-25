import pandas
from sklearn import linear_model

"""
Aprendizado de Máquina
Regressão Múltipla
A regressão múltipla é como a regressão linear,
Mas com mais de um valor independente, o que significa que tentamos prever um valor com base em duas ou mais variáveis.
Como funciona?
Em Python, temos módulos que farão o trabalho para nós.
Comece importando o módulo Pandas ---> import pandas
O módulo Pandas nos permite ler arquivos csv e retornar um objeto DataFrame.
O arquivo destina-se apenas para fins de teste, você pode baixá-lo aqui: data.csv
"""
df = pandas.read_csv("data.csv")

"""
Em seguida, faça uma lista dos valores independentes e chame essa variável X.
Coloque os valores dependentes em uma variável chamada y.
"""
X = df[['Weight', 'Volume']]
y = df['CO2']

"""
Dica: É comum nomear a lista de valores independentes com um X maiúsculo e a lista de valores dependentes com um y minúsculo.
Usaremos alguns métodos do módulo sklearn, então teremos que importar esse módulo também:
from sklearn import linear_model
A partir do módulo sklearn usaremos o LinearRegression()método para criar um objeto de regressão linear.
Este objeto possui um método chamado fit()que toma os valores independentes e dependentes como parâmetros e preenche o objeto de regressão com dados que descrevem o relacionamento:
"""

regr = linear_model.LinearRegression()
regr.fit(X, y)

"""
Agora temos um objeto de regressão pronto para prever os valores de CO2 com base no peso e volume de um carro:
#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
"""
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)