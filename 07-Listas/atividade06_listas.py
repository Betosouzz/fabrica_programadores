# autor: Humberto Lucas
# projeto: listas em Python

#           0        1         2             3
nomes = ['pelé', 'gabigol', 'messi', 'cristiano ronaldo']
print(nomes)

# adicionando um nome na lista
# para retirar as aspas e os colchetes, use *
nomes.append('Pedro')
print(*nomes)

# adicionando um nome em uma posição específica
nomes.insert(4,'Neymar')
print(*nomes)

#modificar uma pessoa da lista
nomes [5] = 'mbappe'
print(*nomes)

# removendo um nome da lista
del nomes[2]
print(*nomes)

# removendo um nome por texto
# buscar o nome e apagar o primeiro que aparecer
nomes.remove('gabigol')
print(*nomes)

# Usando o pop para Mostrar o nome removido
#   0        1               2      3
# pelé  cistriano ronaldo neymar mabappe
removido = nomes.pop(1)
print(f' Após o pop foi removido o nome: {removido}', nomes)

# Limpar a lista
nomes.clear()
print(f' Após o clear a lista é: {nomes}')