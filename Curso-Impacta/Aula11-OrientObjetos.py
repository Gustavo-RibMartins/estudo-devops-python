# modulo = pessoas | objeto = Pessoa
from pessoas import Pessoa
from carros import Carro
from carros import Fusca
from carros import Ferrari

p = Pessoa()
p.nome = "João"

print(p.nome)
p.salvar(p.nome)


c = Carro("Ponte")
print(c.caminho)
c.andar()
# Alterando o valor de caminho
c.caminho = "Praia"
c.andar()

f = Fusca("Avenida")
f.andar()
f.correr()

ferrari = Ferrari("Avenida")
ferrari.andar()