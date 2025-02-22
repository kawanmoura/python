from ..models.produto import Produto
from ..database.database import BancoFake

class produtoController:

    def __init__(self):
        # Conexão com o banco
        self.db = BancoFake()

    def criar_produto(self, nome, preco):
        # Cria o objeto produto e salva no banco
        novo_produto = Produto(nome, preco)
        # Converter para dict (JSON)
        dict_produto = {
            "nome": novo_produto.nome,
            "preco": novo_produto.preco
        }
        # Salvar no banco
        self.db.adicionar_produto(dict_produto)
        print("Produto cadastrado com sucesso!")

    def listar_produtos(self):
        # Listar produtos do banco
        produtos = self.db.listar_produtos()
        return [Produto(**produto) for produto in produtos]
