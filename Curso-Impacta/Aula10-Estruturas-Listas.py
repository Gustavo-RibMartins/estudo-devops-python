lista = [1, 2, 3, 4, 5]

# print da lista toda
print(lista)

# print do segundo item da lista
print(lista[1])

# Lista com laço
for x in lista: print(x)

# Lista com vários valores diferentes

lista_2 = [1, 'Antonio', 3.14, 'String', True]
for x in lista_2: print(x)

# Mutabilidade da lista
print(lista_2)
lista_2[2] = 'PI'
print(lista_2)

# Incluindo novos valores na lista
print(lista_2)
lista_2.append('Novo Valor')
print(lista_2)

# Removendo um item da lista (o último)
print(lista_2)
lista_2.pop()
print(lista_2)

# Removendo um valor especifico da lista
#    remove apenas a primeira ocorrencia do valor
#    se 'Antonio' aparece mais de uma vez, o Python removeria
#    apenas o primeiro valor que aparecesse
print(lista_2)
lista_2.remove('Antonio')
print(lista_2)

# Inserindo novos valores na lista
print(lista_2)
# <list>.insert(<indice>, <valor>)
lista_2.insert(2, 'insert')
print(lista_2)
lista_2.insert(0, 'inicio')
print(lista_2)

# Imprimindo a lista de forma inversa
print(lista_2)
lista_2.reverse()
print(lista_2)

# Ordenando a lista
lista_2.remove(1)
lista_2.remove(True)
# Removemos o int e boolean porque para usar o sort()
# precisamos que na lista tenham apenas itens do mesmo tipo
print(lista_2)
lista_2.sort()
print(lista_2)

# Ordenando a lista de forma reversa
print(lista_2)
lista_2.sort(reverse=True)
print(lista_2)