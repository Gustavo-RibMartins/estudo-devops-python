# Criando um dicionario
d = {}
print(d)

# Inserindo valores no dicionario
d['nome'] = 'Marcos'
d['sobrenome'] = 'Almeida'
d['data_nascimento'] = '18/05/1979'
d['telefone'] = '11998765432'
print(d)

# Removendo itens do dicionario
d.pop('telefone')
print(d)

# Imprimir os valores
print(d.values())

# Imprimira as chaves
print(d.keys())