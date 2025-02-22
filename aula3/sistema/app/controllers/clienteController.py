from ..models.cliente import Cliente
from ..database.database import BancoFake

class clienteController:

    def __init__(self):
        # Conexão com o banco
        self.db = BancoFake()

    def criar_cliente(self, nome, email, idade):
        # Cria o objeto cliente e salva no banco
        novo_cliente = Cliente(nome, email,idade)
        # Converter para dict (JSON)
        dict_cliente = {
            "nome": novo_cliente.nome,
            "email": novo_cliente.email,
            "idade": novo_cliente.idade
        }
        # Salvar no banco
        self.db.adidicionar_cliente(dict_cliente)
        print("Cliente cadastrado com sucesso!")

    def listar_clientes(self):
        print("Listar clientes")