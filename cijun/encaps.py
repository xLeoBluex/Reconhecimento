class Perfil(object):

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print(self.nome) 
        print(self.telefone) 
        print(self.empresa)
        print(self.__curtidas)

    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas

Perfil = Perfil("Gustavo", "Não informado", "Caelum")
Perfil.curtir()
Perfil.curtir()
Perfil.obter_curtidas()
Perfil.imprimir()
