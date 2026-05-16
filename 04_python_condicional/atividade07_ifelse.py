# Autor: Humberto Lucas
# Projeto: Desvio Condicional

# Criação das Variáveis
nome = input('Qual é o seu nome? ')
salario = float(input(f"{nome}, digite seu salário: "))
calculo = salario * 0.10
if calculo > 100:
    print(f"O {nome} tem dinheiro!")
else:
    print(f"O {nome} não tem dinheiro!")
    
