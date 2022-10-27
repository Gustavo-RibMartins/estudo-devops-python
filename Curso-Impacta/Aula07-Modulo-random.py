# Módulo random
import random

# Retorna um número aleatório entre 0 e 1
print(random.random())

# Retorna um inteiro entre o primeiro e segundo parametro
print(random.randint(10, 20))

# Retorna um elemento de uma lista
x = ['Brasil', 'Chile', 'USA', 'Japão']
print(random.choice(x))

# Embaralha os itens de uma lista
x = ['Brasil', 'Chile', 'USA', 'Japão']
print(x)
random.shuffle(x)
print(x)
