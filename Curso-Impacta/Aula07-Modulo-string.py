import string

# Retorna todos os caracteres especiais
# pode ser usado para validar se o usuário digitou pontos
print(string.punctuation)

# Retorna todos os digitos de 0 a 9
# pode ser usado para validar números, como cpf
print(string.digits)

# Retorna hexadecimais
print(string.hexdigits)

# Para Camel Case
print(string.capwords("teste de capitalize no curso"))
