# estudo-devops-python

> Repositório para estudo da linguagem Python.

---

### Conteúdo do Repositório

* [./Curso-Impacta/](https://github.com/Gustavo-RibMartins/estudo-devops-python/tree/main/Curso-Impacta "Curso de Python do MBA da Impacta"): Código-Fonte gerado durante o curso de Python do MBA em Cloud Computing & DevOps da Impacta.

---
### 1. Introdução

Python na versão 2.0 foi criado em 2000 e a versão 3.0 em 2008.

Mac OS e Linux já vem com Python instalado por default, mas é possível instalar o Python ou atualizar a versão acessando o site [python.org](https://www.python.org/ "https://www.python.org/")

#### 1.1. Comandos Úteis:

##### i) type

Sintaxe
```python
type(<var>) # mostra a tipagem da variável
```
Exemplo
```python
type("variavel_teste")
```
Retorno
```python
<class 'str'>
```

##### ii) dir

Sintaxe
```python
dir(<var>) # mostra os métodos aplicáveis a variável
```
Exemplo
```python
dir(100)
```
Retorno
```python
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

##### iii) help

Sintaxe
```python
help(<var>.metodo) # mostra a documentação do método
```
Exemplo
```python
help("test".upper)
```
Retorno
```python
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.
```
---
### 2. Variáveis

No Python, as variáveis são sempre passadas por **referência**, e não por valor.
Por exemplo, se for chamado o método `fillTrash()` que preenche a variável `trash`, tanto o resultado do método quanto a variável assumirão o valor alterado.

![](/Imagens/VarPassRef.png)

No Python não é preciso declarar o tipo da variável.

Utilizamos 3 tipos de dados:

```Python
Inteiros:           10, 2, 50000
Ponto Flutuante:    3.14, 1.2345
String:             "A", "R2D2"
```

#### 2.1. Tipagem Dinâmica

O Python permite que você faça a atribuição de uma variável sem informar o seu tipo, apenas passando o seu valor.

```Python
a=10
type(a)
# output
<class 'int'>
```

#### 2.2. Tipagem Forte

Por não precisar que o tipo da variável seja declarado, para o Python é essencial que a variável receba valores e chamadas de métodos consistentes com o valor com o qual é iniciada.

por exemplo, imagine que tentemos somar um inteiro `varInt` com uma string `varString`, obteremos o seguinte erro:

```Python
varInt = 10
varString = 'Texto'
varInt + varString
# output
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    varInt + varString
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
Entretanto, o tipo da variável pode mudar ao longo do tempo:
```Python
a = 10
type(a)
<class 'int'>
# reatribuição
a = '10'
type(a)
<class 'str'>
```

---
### 3. Operadores

#### 3.1. Aritméticos

![Operadores Aritméticos](./Imagens/OperAritmeticos.png "Operadores Aritméticos")

#### 3.2. Relacionais

![Operadores Relacionais](./Imagens/OperRelacionais.png "Operadores Relacionais")

#### 3.3. Lógicos

![Operadores Lógicos](./Imagens/OperLogicos.png "Operadores Lógicos")

---
### 4. Entrada e Saída de Dados

Para receber dados de entrada, utiliza=se a função `input()`, que retorna uma string:

```python
a = input("Digite um número inteiro: ")
b = input("Digite outro número inteiro: ")

print(a + b)

Supondo que a = 20 e b = 35, a saída é: 2035
```

Podemos imprimir dados separando os argumentos na função `print()` por vírgula:

```python
print("Imprimindo", "com", "Python")

# Saída
Imprimindo com Python
```

**Impressão com marcadores**

```python
a = 10
print("Tirei %d na prova" %a)

# Saída
Tirei 10 na prova
```

Os marcadores são:
- %d = para inteiros
- %s = para strings
- %f = para ponto flutuante

Para ponto flutuante, pode-se definir o número de casas decimais substituindo o valor de n em `%.nf`

```python
print("A nota é: %.2f" %8.9876)

# Saída
A nota é: 8.99
```

Também é possível usar vários marcadores usando listas:

```python
print("inteiro: %d, float: %.3f, string: %s" %(2, 3.12345, "texto"))

# Saída
inteiro: 2, float: 3.123, string: texto
```

---
### 5. Estrutura Condicional
