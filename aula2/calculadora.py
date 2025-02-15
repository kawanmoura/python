
def menu():
    print("Menu da Calculadora")
    print("1- Somar")
    print("2- Subtrair")
    print("3- Sair")

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def VerificaOpção(opcao):
    if opcao == 1:
        num1 = float(input("Digite o número 1: "))
        num2 = float(input("Digite o número 2: "))
        print(somar(num1 + num2))
    elif opcao == 2:
        num1 = float(input("Digite o número 1: "))
        num2 = float(input("Digite o número 2: "))
        print(subtrair(num1 + num2))

def calculadora():
    while True:
        menu()
        opcao = int(input("Escolha uma opção: "))
        VerificaOpção(opcao)

calculadora()