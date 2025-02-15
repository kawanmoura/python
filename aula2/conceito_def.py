
def carro_kawan():
    print("Lancer GT")

carro_kawan()

def escrever_carro(nome):
    print(nome)
escrever_carro("Lancer GT 2001")

def somar_numeros(num1, num2):
    return num1 + num2

resultado = somar_numeros(4,4)
print("O resultado é: ", resultado)

#_______________________________________________
def verificaIdade(idade):
    if idade >= 18:
        return "Pode ver o filme"
    else:
        return "Não pode ver o filme"

print("Digite sua idade: ")
idade = int(input())

resultado = verificaIdade(idade)

print(resultado)