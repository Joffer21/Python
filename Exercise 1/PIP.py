"""
    Python PIP
    O que é o PIP?
    O PIP é um gerenciador de pacotes, para pacotes Python ou módulos, se preferir.
    Obs.:Se você tiver o Python versão 3.4 ou posterior, o PIP será incluído por padrão.
    O que é um Pacote?
    Um pacote contém todos os arquivos necessários para um módulo.
    Módulos são bibliotecas de código Python que você pode incluir em seu projeto.
"""
import camelcase

c = camelcase.CamelCase()
txt = "Hello world"

print(c.hump(txt))