import csv

# criar e escrever um arquivo TXT
# w -> Write -> Escrita
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome,Idade,Cidade\n")
    arquivo.write("Alberto,92,Xique-Xique/BA")
    arquivo.write("Arthur,28,Arraial/RJ\n")
    arquivo.write("Matheus,28,Cotia/SP")

# Ler o conteúdo
# r -> Read -> Ler
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("Conteúdo do arquivo txt: ")
    print(arquivo.read())

# Criando arquivo csv
dados = [
    ["Nome", "Idade", "Cidade"],
    ["Carlos", "32", "Santa Isabel"],
    ["Diego", "19", "Americana"],
    ["Kawan", "18", "Vargem Grande Paulista"]
]

# Criar arquivo csv
with open("dados.csv", "w", newline="", encoding="utf-8") as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerow(dados)

# Ler o arquivo csv
with open("dados.csv", "r", encoding="utf-8") as csvarquivo:
    leitor = csv.reader(csvarquivo)
    print("\nConteúdo do Arquivo CSV")
    for linha in leitor:
        print(linha)

