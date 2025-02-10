
from database.database import Database

class Reserva:
    def __init__(self, usuario_nome, livro_nome):
        self.usuario_nome = usuario_nome
        self.livro_nome = livro_nome

    def realizar(self):
        db = Database()
        usuario = db.execute('SELECT id FROM users WHERE name = %s', (self.usuario_nome,))
        livro = db.execute('SELECT id FROM books WHERE name = %s', (self.livro_nome,))
        
        if not usuario:
            print('Erro: Usuário não encontrado.')
            return
        if not livro:
            print('Erro: Livro não encontrado.')
            return
        
        db.execute('INSERT INTO reservations (bookId, userId) VALUES (%s, %s)', (livro[0][0], usuario[0][0]))
        print('Reserva feita com sucesso!')