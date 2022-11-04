# criar um programa que recebe uma lista de inteiros e retorno o numero da lista que mais se repete
# e quantas vezes ele se repete

entrada = int(input("Digite um inteiro positivo: "))
lista = []

while entrada >= 0:
    lista.append(entrada)
    entrada = int(input("Digite um inteiro positivo: "))
lista.sort()

numero = lista[0]
repeticoes = 1

for x in lista:
    if lista.count(x) > repeticoes:
        numero = lista[x]
        repeticoes = lista.count(x)

print(lista)
print("O número mais frequente é %d e se repete %d vezes!" %(numero, repeticoes))
