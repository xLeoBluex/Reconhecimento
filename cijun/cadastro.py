import customtkinter as ctk

def abrir_nova_pagina():
    
    
    janela = ctk.CTk()
    
    janela.title("Home")
    # Tamanho da janela
    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela (70% da tela)
    largura_janela = int(largura_tela * 0.7)
    altura_janela = int(altura_tela * 0.7)

    # Centralizar a janela
    janela.geometry(f"{largura_janela}x{altura_janela}+{int((largura_tela - largura_janela) / 2)}+{int((altura_tela - altura_janela) / 2)}")

    # Frame de fundo que ocupa toda a janela
    bg_frame = ctk.CTkFrame(janela, fg_color='#202033', bg_color='#202033')
    bg_frame.place(relwidth=1, relheight=1)

    # Frame principal para centralizar os componentes e ajustar o tamanho
    frame = ctk.CTkFrame(master=janela,
         width=980,
         height=610,
         corner_radius=30,
         fg_color='#2B2B30',
         bg_color='#202033')

    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    frame.pack_propagate(False)


    # Inicia a tela
    janela.mainloop()

