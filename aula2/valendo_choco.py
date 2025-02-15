print("Bem-Vindo(a) ao consolidador de palíndromos!")
palavra = input("Digite uma palavra: ")

palavra_formatada = ''.join(palavra.split()).lower()

if palavra_formatada == palavra_formatada[::-1]:
    print("É palíndromo sim")
else:
    print("Não é um palíndromo")