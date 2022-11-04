# fazer um programa que recebe um inteiro n e calcule o seu fatoria n!

n = int(input("Digite um inteiro: "))
fatorial = 1

while n > 0:
    fatorial = fatorial * n
    n = n - 1

print("Fatorial = %d" %fatorial)
