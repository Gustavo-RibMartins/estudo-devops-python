# Função para somar

def somar (numero1, numero2):
    print(numero1 + numero2)

# Função para subtrair

def subtrair(n1, n2):
    return n1 - n2

# kwargs = dicionário de chave e valor

def imprime_parametros (**kwargs):
    for key, value in kwargs.items():
        print("%s = %s" %(key, value))


numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

somar(numero1, numero2)
print(subtrair(numero1, numero2))

imprime_parametros(nome="Ana", Sobrenome="Maria", Apelido="Aninha", DataNas="02/06/1996")
