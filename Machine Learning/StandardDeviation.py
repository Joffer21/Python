import numpy

"""
Aprendizado de Máquina - Desvio Padrão
O que é Desvio Padrão?
O desvio padrão é um número que descreve a dispersão dos valores.
Um desvio padrão baixo significa que a maioria dos números está próximo do valor médio (média).
Um desvio padrão alto significa que os valores estão espalhados por uma faixa mais ampla.
Exemplo: Desta vez registramos a velocidade de 7 carros:

speed = [86,87,88,86,87,85,86]

O desvio padrão é:
0.9

O que significa que a maioria dos valores está dentro do intervalo de 0,9 do valor médio, que é 86,4.
Façamos o mesmo com uma seleção de números com um intervalo mais amplo:

speed = [32,111,138,28,59,77,97]

O desvio padrão é:
37.85

Isso significa que a maioria dos valores está dentro da faixa de 37,85 do valor médio, que é 77,4.
Como você pode ver, um desvio padrão mais alto indica que os valores estão espalhados por uma faixa mais ampla.
O módulo NumPy possui um método para calcular o desvio padrão:

Exemplo:
Use o método NumPy std() para encontrar o desvio padrão:
"""

#speed = [86,87,88,86,87,85,86]
speed = [32,111,138,28,59,77,97]

x = numpy.std(speed)

print(x)

#----------------------------------------------------------------------

"""
variância
A variação é outro número que indica como os valores estão espalhados.
Na verdade, se você tirar a raiz quadrada da variância, obterá o desvio padrão!
Ou o contrário, se você multiplicar o desvio padrão por ele mesmo, obtém a variância!
Para calcular a variância, você deve fazer o seguinte:

1. Encontre a média:

(32+111+138+28+59+77+97) / 7 = 77.4

2. Para cada valor: encontre a diferença da média:

 32 - 77.4 = -45.4
111 - 77.4 =  33.6
138 - 77.4 =  60.6
 28 - 77.4 = -49.4
 59 - 77.4 = -18.4
 77 - 77.4 = - 0.4
 97 - 77.4 =  19.6

3. Para cada diferença: encontre o valor ao quadrado:

(-45.4)2 = 2061.16
 (33.6)2 = 1128.96
 (60.6)2 = 3672.36
(-49.4)2 = 2440.36
(-18.4)2 =  338.56
(- 0.4)2 =    0.16
 (19.6)2 =  384.16
4. A variância é o número médio dessas diferenças ao quadrado:

(2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2

Felizmente, o NumPy tem um método para calcular a variância:

Exemplo:
Use o método NumPy var()para encontrar a variância:
"""

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)

print(x)

#--------------------------------------------------------------------------------

"""
Desvio padrão
Como aprendemos, a fórmula para encontrar o desvio padrão é a raiz quadrada da variância:

√1432.25 = 37.85
Ou, como no exemplo anterior, use o NumPy para calcular o desvio padrão:

Exemplo
Use o método NumPy std()para encontrar o desvio padrão:
"""

speed = [32,111,138,28,59,77,97]

x = numpy.std(speed)

print(x)

"""
Símbolos
O Desvio Padrão é frequentemente representado pelo símbolo Sigma: σ
A variância é frequentemente representada pelo símbolo Sigma ao quadrado: σ 2
Resumo do capítulo
O Desvio Padrão e a Variância são termos frequentemente usados ​​em Machine Learning, por isso é importante entender como obtê-los e o conceito por trás deles.
"""