# Se a classe não tiver herança, entre parenteses vai o "pai" object
# Precisamos declarar uma herança nos paretentes da classe

class Pessoa(object):
    nome = None

    def salvar(self, x): # "self" refere-se a propria classe
        self.nome = x
        print("Salvando", self.nome)

