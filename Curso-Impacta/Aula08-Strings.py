print("Texto para ser fatiado"[0:10])

print("Texto para ser fatiado"[3:10])
print("Texto para ser fatiado"[3:])

# Para pular de 3 em 3 letras
print("Texto para ser fatiado"[0:10:3])

# Fatiamento com valor negativo
print("Texto para ser fatiado"[::-1])

# Para saber se uma string começa ou termina com uma letra
nome = "Gustavo"

print(nome.startswith('G'))
print(nome.startswith('g')) # python é case sensitive
print(nome.endswith('o'))

# Replace
print(nome.replace('v','b'))

# Split
texto = "Testando split no python"
s = texto.split()
print(s)

# Split informando o delimitador
texto = "Testando;novos;delimitadores"
s = texto.split(";")
print(s)

# Join
data = ['18','05','1979']
print('/'.join(data))
