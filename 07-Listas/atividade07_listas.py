# Autor: Humberto Lucas
# Projeto: Programa Cadastro


#           0        1         2             3
nomes = ['pelé', 'gabigol', 'messi', 'cristiano ronaldo']
print(nomes)

# adicionando um nome na lista
# para retirar as aspas e os colchetes, use *
nomes.append('Pedro')
print(*nomes)


# removendo um nome por texto
# buscar o nome e apagar o primeiro que aparecer
nomes.remove('gabigol')
print(*nomes)



