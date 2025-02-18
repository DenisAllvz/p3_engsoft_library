from database.database import Database

class Livro:
    def __init__(self, nome, categoria, autor):
        self.nome = nome
        self.categoria = categoria
        self.autor = autor

    def salvar(self):
        db = Database()
        existente = db.execute("SELECT id FROM books WHERE name = %s", (self.nome,))
        if existente:
            print("Erro: Livro já cadastrado.")
            return
        db.execute('INSERT INTO books (name, category, author) VALUES (%s, %s, %s)', (self.nome, self.categoria, self.autor))
        print('Livro cadastrado com sucesso!')
