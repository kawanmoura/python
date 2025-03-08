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
    try:
        novo_id = model.insert_user(nome, idade, email)
    except ValueError as e:
        model.close_connection()
        return str(e)
    model.close_connection()
    return novo_id

def deletar_usuario(user_id):
    """ Deletar usuario no banco """
    model = UsuarioModel()
    linhas = model.delete_user_by_id(user_id)
    model.close_connection()
    return linhas

def atualizar_usuario(user_id, nome, idade, email):
    """ Atualizar usuario no banco """
    model = UsuarioModel()
    linhas = model.update_user_by_id(user_id, nome, idade, email)
    model.close_connection()
    return linhas

def obter_usuario(user_id):
    """ Obter usuario no banco pelo ID """
    model = UsuarioModel()
    usuario = model.get_user_by_id(user_id)
    model.close_connection()
    return usuario
