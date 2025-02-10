
from database.database import Database

class Usuario:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def salvar(self):
        db = Database()
        existente = db.execute("SELECT id FROM users WHERE email = %s", (self.email,))
        if existente:
            print("Erro: Usuário já cadastrado.")
            return
        db.execute('INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)', (self.nome, self.email, self.telefone))
        print('Usuário cadastrado com sucesso!')