class Carro(object):

    def __init__(self, caminho):
        self.caminho = caminho

    def andar(self):
        print('Andando pela', self.caminho)


class Fusca(Carro):

    def __init__(self, caminho):
        self.caminho = caminho

    def correr(self):
        self.caminho = "Pista"
        super(Fusca, self).andar()
    
class Ferrari(Carro):

    def __init__(self, caminho):
        self.caminho = caminho
    
    def andar(self):
        print("correndo muito")