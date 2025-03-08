from src.controller import produto_controller, usuario_controller

def exibir_menu():
    print("\nMAREA TOCA TUDO LTDA")
    print("\n==== MENU ====")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Atualizar Produto")
    print("4 - Deletar produto")
    print("5 - Buscar produto unico")
    print("6 - Cadastrar Usuario")
    print("7 - Listar Usuarios")
    print("8 - Deletar Usuario")
    print("0 - Sair")

def listar_produtos():
    print("\n--- Lista de Produtos ---")
    produtos = produto_controller.listar_produtos()
    if produtos:
        for produto in produtos:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preco: {produto['preco']}")
    else:
        print("Não existe produtos cadastrados")

def cadastrar_produto():
    print("\n--- Cadastrar Produto ---")
    nome = input("Digite o nome: ")
    preco = input("Digite o valor: ")
    novo_id = produto_controller.cadastrar_produto(nome, preco)
    print(f"Produto cadastrado com sucesso com o novo ID {novo_id}.")

def opcao_atualizar():
    print("\nATUALIZANDO O PRODUTO")
    produto_id = input("Digite o ID do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")

    linhas = produto_controller.atualizar_produto(produto_id, nome, preco)
    if linhas > 0:
        print("Produto atualizado com sucesso!")
    else:
        print("Nenhum produto foi atualizado!")

def deletar_produto():
    print("\n--- Deletar Produto ---")
    produto_id = input("Digite o ID do produto: ")
    linhas = produto_controller.remover_produto(produto_id)
    if linhas > 0:
        print("Produto deletado com sucesso!")
    else:
        print("Nenhum produto foi deletado!")

def buscar_produto_unico():
    print("\n--- Buscar Produto Unico ---")
    produto_id = input("Digite o ID do produto: ")
    produto = produto_controller.obter_produto(produto_id)
    if produto:
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preco: {produto['preco']}")
    else:
        print("Produto não encontrado")

def cadastrar_usuario():
    print("\n--- Cadastrar Usuario ---")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    email = input("Digite o email: ")
    resultado = usuario_controller.cadastrar_usuario(nome, idade, email)
    if isinstance(resultado, int):
        print(f"Usuario cadastrado com sucesso com o novo ID {resultado}.")
    else:
        print(f"Erro ao cadastrar usuario: {resultado}")

def listar_usuarios():
    print("\n--- Lista de Usuarios ---")
    usuarios = usuario_controller.listar_usuarios()
    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")
    else:
        print("Não existe usuarios cadastrados")

def deletar_usuario():
    print("\n--- Deletar Usuario ---")
    user_id = input("Digite o ID do usuario: ")
    linhas = usuario_controller.deletar_usuario(user_id)
    if linhas > 0:
        print("Usuario deletado com sucesso!")
    else:
        print("Nenhum usuario foi deletado!")

# main -> Inicializar o projeto
def main():
    # While True para repetir mesmo que a opção digitado esteja errada
    while True:

        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_produto()
        elif opc == "2":
            listar_produtos()
        elif opc == "3":
            opcao_atualizar()
        elif opc == "4":
            deletar_produto()
        elif opc == "5":
            buscar_produto_unico()
        elif opc == "6":
            cadastrar_usuario()
        elif opc == "7":
            listar_usuarios()
        elif opc == "8":
            deletar_usuario()
        elif opc == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção Inválida")

if __name__ == '__main__':
    main()
