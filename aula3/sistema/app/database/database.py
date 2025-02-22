import json # Lidar com arquivo JSON
from pathlib import Path # Lidar com caminhos WIN


class BancoFake:

    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": [], "produtos": []}
        self._carregar()

    def _carregar(self):
        """
        Carrega dados do arquivo JSON, se existir,
        caso não exista, inicia com dados vazios
        """
        caminho = Path(self.arquivo_db)
        if caminho.is_file():
            # Abrindo arquivo no modo leitura em UTF-8 (PT-BR)
            with open(caminho, 'r', encoding="utf-8") as data:
                # Salvando dados que ja existem no arquivo
                # Na variável dados
                self.dados = json.load(data)
        else:
            self._salvar()

    def _salvar(self):
        """ 
        Salvar o conteúdo de self.dados no arquivo JSON
        """
        with open(self.arquivo_db, 'w', encoding="utf-8") as f:
            # Realizando DUMP (Python para JSON) para salvar no banco
            json.dump(self.dados, data, ensure_ascii=False, indent=4)

    def adidicionar_cliente(self, cliente_dict):
        self.dados["clientes"].append(cliente_dict)
        self._salvar()

    def listar_clientes(self):
        return self.dados["clientes"]