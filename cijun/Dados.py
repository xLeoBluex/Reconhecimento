class Perfil(object):

    def __init__(self, nome, telefone, CPF):
        self.nome = nome
        self.__telefone = telefone
        self.__CPF = CPF
        
    def imprimirAdm(self):
        print(self.nome) 
        print(self.__telefone) 
        print(self.__CPF)
    
    def imprimirUser(self):
        print(self.nome) 
        
Perfil = Perfil("Gustavo", "(11) 95845-2477", "444.444.444-87")