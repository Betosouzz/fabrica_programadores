# Autor: Humberto Lucas
# Projeto: Desvio Condicional

# Criação das Variáveis
nome = input('Qual é o seu nome? ')
idade = int(input('Quaantos anos você tem? '))
if idade>=18:
    print(f'{nome}, você tem carteira de motorista? pode dirigir!')
else:
    print(f"{nome}, você não tem idade suficiente para dirigir")
