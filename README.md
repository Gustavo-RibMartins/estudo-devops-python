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
type(<var>) # mostra a tipagem da variavel
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
dir(<var>) # mostra os metodos aplicaveis a variavel
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