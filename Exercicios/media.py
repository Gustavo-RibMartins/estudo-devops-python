# desenvolver um codigo que recebe uma lista de numeros e calcula a média deles
# o usuario pode digitar n numeros na entrada, mas quando digitar um numero negativo
# o programa deve retornar o valor da media dos numeros inseridos, desconsiderando o
# numero negativo inserido

tmp = 0
lista = []
soma = 0
itens = 0

while tmp >= 0:
    tmp = float(input("Digite um número: "))
    if tmp >= 0:
        lista.append(tmp)

for x in range(len(lista)):
    soma =  soma + lista[x]
    itens = x + 1

if itens != 0:
    media = soma / (1. * itens)

    print("Lista =", lista)
    print("Soma = %.2f" %soma)
    print("Itens = %d" %itens)
    print("A média é %.2f" %media)
else:
    print("Impossível de calcular a média. Nenhum valor válido informado.")