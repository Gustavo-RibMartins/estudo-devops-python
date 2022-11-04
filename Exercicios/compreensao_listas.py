# fazer um programa que recebe uma lista de inteiros positivos e retorna duas novas listas
# uma com os elementos pares elevados ao quadrado e outra com os elementos impares ao cubo

entrada = int(input("Digite um inteiro positivo: "))
lista_in = []

while entrada >= 0:
    lista_in.append(entrada)
    entrada = int(input("Digite um inteiro positivo: "))
lista_in.sort()

lista_par = [x**2 for x in lista_in if x % 2 == 0]
lista_impar = [x**3 for x in lista_in if x % 2 != 0]

print(lista_in)
print(lista_par)
print(lista_impar)
