import Dados

adm = "admin"
senhaAdm = "123456789"


user = "user"
senhaUser = "123456789"

Log = input("Login: ")
Senha = input("Senha: ")

if Log == adm and Senha == senhaAdm:
    Dados.Perfil.imprimirAdm()
    print("Você entrou como Adm")

elif Log == user and Senha == senhaUser:
    Dados.Perfil.imprimirUser()
    print("Você entrou como Usuario")

else:
    print("Login e senha errado")