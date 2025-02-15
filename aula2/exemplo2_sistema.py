# Sistema de desconto de Veículos
# Solicite o nome do veículo
# E o preço do veículo
# Se o preço > 80k -> 60% de desconto
# Se o preço > 50k -> 30% de desconto
# Se o preço < 50k -> Não existe desconto
# Sistema de desconto de Veículos
# Solicita o nome e o preço do veículo

nome_veiculo = input("Digite o nome do veículo: ")
preco_veiculo = float(input("Digite o preço do veículo: R$ "))

if preco_veiculo >= 80000:
    desconto = 0.60  # 60% de desconto
elif preco_veiculo >= 50000:
    desconto = 0.30  # 30% de desconto
else:
    desconto = 0  # Sem desconto

preco_com_desconto = preco_veiculo * (1 - desconto)

if desconto > 0:
    print(f"O veículo {nome_veiculo} recebeu um desconto de {desconto * 100}%")
    print(f"Preço original: R$ {preco_veiculo}")
    print(f"Preço com desconto: R$ {preco_com_desconto}")
else:
    print(f"O veículo {nome_veiculo} não tem desconto.")
    print(f"Preço do veículo: R$ {preco_veiculo}")