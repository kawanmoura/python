print("Bam-Vindo  ao sistema do Cinema")
print("Digite sua idade: ")
idade = int(input())

if idade >= 18:
    print("Pode assistir")
else:
    print("Pode não fiot")

# Criar novo arquivo
# Desenvolver um sistema que recebe
# Valor de A, Valor de B e Valor de C
# Calcular a Bhaskara
# Delta = b**2 - 4*a*c
# ax²+bx+c=0
# x1 = (-b + delta ** 0.5) / 2*a
# x2 = (-b - delta ** 0.5) / 2*a
# Bhaskara
import math

print("Bem-Vindo ao sistema de Bhaskara")
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b**2 - 4 * a * c
print(f"Delta: {delta}")

raiz_delta = math.sqrt(delta) #Função de Delta
print(f"Raiz de Delta: {raiz_delta}")

x1 = (-b + raiz_delta) / 2 * a
x2 = (-b - raiz_delta) / 2 * a

print(f"O valor de x1 é: {x1}")
print(f"O valor de x2 é: {x2}")