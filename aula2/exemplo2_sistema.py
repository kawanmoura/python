# Criar novo arquivo
# Desenvolver um sistema que recebe
# Valor de A, Valor de B e Valor de C
# Calcular a Bhaskara
# Delta = b**2 - 4*a*c
# ax²+bx+c=0
# x1 = (-b + delta ** 0.5) / 2*a
# x2 = (-b - delta ** 0.5) / 2*a
# Bhaskara

print("Bem-Vindo ao sistema de Bhaskara")
print("Digite o valor de A: ")
a = float(input())
print("Digite o valor de B: ")
b = float(input())
print("Digite o valor de C: ")
c = float(input())

delta = b**2 - 4*a*c

if delta < 0:
    print("Não tem raiz real")
else:
    x1 = (-b + delta ** 0.5) / 2*a
    x2 = (-b - delta ** 0.5) / 2*a
    print(f"O valor de x1 é: {x1}")
    print(f"O valor de x2 é: {x2}")