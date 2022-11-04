# receber uma serie de numeros inteiros ate o usuario digitar um numero negativo
# calcular a soma, media, maior e menor valor e quantidade de elemetos da lista

entrada = int(input("Digite um inteiro positivo: "))
lista = []

while entrada >= 0:
    lista.append(entrada)
    entrada = int(input("Digite um inteiro positivo: "))

soma = sum(lista)
qtde_elementos = len(lista)
maximo = max(lista)
minimo = min(lista)
media = soma / (1. * qtde_elementos)
lista.sort()

print(lista)
print("Soma = %d" %soma)
print("Quantidade de Elementos = %d" %qtde_elementos)
print("Média = %.2f" %media)
print("Máximo = %d" %maximo)
print("Mínimo = %d" %minimo)
