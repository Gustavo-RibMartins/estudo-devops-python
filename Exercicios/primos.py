# fazer um programa que recebe um inteiro n e devolve uma lista com todos os numeros
# primos de 1 até n

def primo(n):
    qtde_divisores = 0
    i = 1

    while i <= n:
        if n % i == 0:
            qtde_divisores = qtde_divisores + 1
        i = i + 1
    if qtde_divisores == 2 or n == 1:
        return 1
    else:
        return 0

n = int(input("Digite um inteiro: "))
i = 1
lista = []

while i <= n:
    if primo(i) == 1:
        lista.append(i)
    i = i + 1

print(lista)

