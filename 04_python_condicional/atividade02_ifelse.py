# Autor: Humberto Lucas
# Projeto: Desvio Condicional

# Criação das Variáveis
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
if idade>=18:
    print(f'{nome} é maior de idade')
else:
    print(f"{nome} é menor de idade")
