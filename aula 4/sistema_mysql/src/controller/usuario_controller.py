from ..model.usuario_model import UsuarioModel

def listar_usuarios():
    """ Retorna a lista de todos os usuarios (dict) """
    model = UsuarioModel()
    usuarios = model.get_all_users()
    model.close_connection()
    return usuarios

def cadastrar_usuario(nome, idade, email):
    """ Cadastrar usuario no banco """
    model = UsuarioModel()
    novo_id = model.insert_user(nome, idade, email)
    model.close_connection()
    return novo_id
