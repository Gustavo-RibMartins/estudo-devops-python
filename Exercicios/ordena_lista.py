# programa que recebe uma lista de inteiros, e imprime eles em ordem e na ordem reversa
# o programa para de aceitar entradas quando um valor negativo e passado pelo usuario

entrada = int(input("Digite um inteiro positivo: "))
lista = []

while entrada >= 0:
    lista.append(entrada)
    entrada = int(input("Digite um inteiro positivo: "))

print(lista)
lista.sort()
print(lista)
lista.reverse()
print(lista)

print(lista[::-1])
