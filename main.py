'''biblioteca/
│── database/
│   ├── database.py
│
│── models/
│   ├── livro.py
│   ├── usuario.py
│   ├── reserva.py
│
│── strategy/
│   ├── search_strategy.py
│
│── main.py///'''

import questionary
from models.livro import Livro
from models.usuario import Usuario
from models.reserva import Reserva
from strategy.search_strategy import SearchByTitle, SearchByAuthor, SearchByCategory
from database.database import Database

# Criação de instâncias fora do loop principal
livro = Livro(nome="", categoria="", autor="")
usuario = Usuario(nome="", email="", telefone="")
reserva = Reserva(usuario_nome="", livro_nome="")

while True:
    action = questionary.select(
        "O que você deseja fazer?",
        choices=['Cadastrar livro', 'Cadastrar usuário', 'Fazer uma reserva', 'Buscar um livro', 'Sair']
    ).ask()

    if action == "Cadastrar livro":
        livro.nome = input("Digite o nome do livro: ")
        livro.categoria = questionary.select("Qual a categoria do livro?", choices=['Esporte', 'Ficção', 'Educação', 'Fantasia', 'Diversa']).ask()
        livro.autor = input("Qual o nome do autor do livro? ")
        livro.salvar()

    elif action == "Cadastrar usuário":
        usuario.nome = input("Digite seu nome: ")
        usuario.email = input("Digite seu email: ")
        usuario.telefone = input("Digite o número do seu telefone: ")
        usuario.salvar()

    elif action == "Fazer uma reserva":
        reserva.usuario_nome = input("Digite o nome do usuário: ")
        reserva.livro_nome = input("Digite o título do livro: ")
        reserva.realizar()

    elif action == "Buscar um livro":
        search_type = questionary.select(
            "Como você gostaria de buscar o livro?",
            choices=['Buscar por Título', 'Buscar por Autor', 'Buscar por Categoria']
        ).ask()

        search_strategy = None
        search_term = ""
        
        if search_type == 'Buscar por Título':
            search_strategy = SearchByTitle()
            search_term = input("Digite o título do livro: ")
        elif search_type == 'Buscar por Autor':
            search_strategy = SearchByAuthor()
            search_term = input("Digite o nome do autor: ")
        elif search_type == 'Buscar por Categoria':
            search_strategy = SearchByCategory()
            search_term = questionary.select("Escolha a categoria do livro:", choices=['Esporte', 'Ficção', 'Educação', 'Fantasia', 'Diversa']).ask()

        resultados = search_strategy.search(search_term)
        if not resultados:
            print("Nenhum livro encontrado.")
        else:
            for livro in resultados:
                print(livro)

    elif action == "Sair":
        print("Saindo...")
        db = Database()
        try:
            db.cursor.close()
            db.connection.close()
        except Exception as e:
            print("Erro ao fechar a conexão:", e)
        break
    else:
        print("Opção inválida. Tente novamente.")
