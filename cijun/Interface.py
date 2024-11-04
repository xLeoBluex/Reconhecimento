import customtkinter as ctk
import cadastro  # Importa o arquivo da nova página

# Dados de exemplo para login
adm = "admin"
senhaAdm = "123456789"
user = "user"
senhaUser = "123456789"

# Função de login
def loginApp():
    Log = login.get()
    Senha = senha.get()
    if Log == adm and Senha == senhaAdm:
        janela.destroy()  # Fecha a janela atual
        cadastro.abrir_nova_pagina()  # Redireciona para a nova página
    elif Log == user and Senha == senhaUser:
        janela.destroy()  # Fecha a janela atual
        cadastro.abrir_nova_pagina()  # Redireciona para a nova página
    else:
        texto = "Credenciais inválidas!"
        label = ctk.CTkLabel(janela, text=texto, fg_color='#202033', text_color='red')
        label.pack(pady=20)

# Função para estilizar parcialmente o texto do label
def create_label_with_link(texto, texto_link, funcao, frame):
    label_frame = ctk.CTkFrame(frame, fg_color='#2B2B30')
    label_frame.pack(pady=5)

    label = ctk.CTkLabel(label_frame, text=texto, fg_color='#2B2B30', text_color='white', font=("Open Sans", 25, "bold"))
    label.pack(side="left")

    link = ctk.CTkLabel(label_frame, text=texto_link, fg_color='#2B2B30', text_color='#38B6FF', cursor="hand2", font=("Open Sans", 25, "bold"))
    link.pack(side="left")
    link.bind("<Button-1>", lambda e: funcao())

# Função placeholder para clique
def esqueci_senha():
    print("Esqueci a senha clicado.")

def criar_conta():
    print("Criar conta clicado.")

# Criar janela
janela = ctk.CTk()
janela.title("Login")

# Obter as dimensões da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Definir o tamanho da janela (70% da tela)
largura_janela = int(largura_tela * 0.8)
altura_janela = int(altura_tela * 0.75)

# Centralizar a janela
janela.geometry(f"{largura_janela}x{altura_janela}+{int((largura_tela - largura_janela) / 2)}+{int((altura_tela - altura_janela) / 2)}")

# Frame de fundo que ocupa toda a janela
bg_frame = ctk.CTkFrame(janela, fg_color='#202033', bg_color='#202033')
bg_frame.place(relwidth=1, relheight=1)

# Frame principal para centralizar os componentes e ajustar o tamanho
frame = ctk.CTkFrame(master=janela, width=730, height=635, corner_radius=50, fg_color='#2B2B30',bg_color='#202033', border_color='#777784', border_width=4)

frame.place(relx=0.32, rely=0.18, relwidth=0.37, relheight=0.65)
frame.pack_propagate(False)

# Criação dos componentes da interface
email_label = ctk.CTkLabel(frame, text="Email ou Nome de Usuário", fg_color='#2B2B30', text_color='white', font=("Open Sans", 25, "bold"))
email_label.place(relx=0.2, y=75, anchor="center")  # Centraliza o label no meio do frame, com Y = 50

login = ctk.CTkEntry(frame, width=650, font=("Open Sans", 18, "bold"), fg_color='#777784', text_color='#29292E')
login.pack(pady=5)

senha_label = ctk.CTkLabel(frame, text="Senha", fg_color='#2B2B30', text_color='white', font=("Open Sans", 25, "bold"))
senha_label.place(relx=0.1, y=270, anchor="center")

senha = ctk.CTkEntry(frame, show="*", width=650, height=40 , font=("Open Sans", 18, "bold"), fg_color='#777784', text_color='#29292E')
senha.place(relx=0.5, y=340, anchor="center")

# Variável para controlar o estado da senha
mostrar = False

# Checkbox para mostrar senha
def toggle_password():
    global mostrar
    mostrar = not mostrar  # Alterna o estado
    senha.configure(show='' if mostrar else '*')  # Alterna a visibilidade

mostrar_label = ctk.CTkLabel(frame, text="Mostrar-me a Senha", fg_color='#2B2B30', text_color='white', font=("Open Sans", 25, "bold"))
mostrar_label.place(relx=0.05, y=400)
mostrar_senha = ctk.CTkCheckBox(frame, text="", fg_color='#2B2B30', text_color='white', command=toggle_password, font=("Open Sans", 25, "bold"))
mostrar_senha.place(relx=0.41, y=402)

# Criar label com "Esqueceu a Senha?" logo abaixo do "Mostrar-me a Senha"
create_label_with_link("Esqueceu a Senha?", "Clique Aqui!", esqueci_senha, frame)

# Criar um frame para o botão de login e o link "Não tem uma conta ainda?"
bottom_frame = ctk.CTkFrame(frame, fg_color='#2B2B30')
bottom_frame.pack(pady=20)

# botão de login
button = ctk.CTkButton(bottom_frame, text="Login", command=loginApp, fg_color='#003C99', text_color='white', font=("Open Sans", 22, "bold"), width=100)
button.pack(side="left", padx=10)

# Criar label com "Não tem uma conta ainda?" ao lado do botão de login
create_label_with_link("Não tem uma conta ainda?", "Clique Aqui!", criar_conta, bottom_frame)

# Inicia a tela
janela.mainloop()
