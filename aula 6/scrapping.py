import requests # Responsável por enviar a requisição
from bs4 import BeautifulSoup # Responsável por tratar a requisição

# class -> feed-post-link

#URL do Site
url = "https://droper.app/marca/nike"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64, x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Fazendo requisição HTTP
resposta = requests.get(url, headers)

# verificar se deu tudo certo
if resposta.status_code == 200:
    # código 200 -> sucesso
    print("Requisição feita com sucesso.")
    # print(resposta.text)
    # preenchendo nossa sopa
    soup = BeautifulSoup(resposta.text, "html.parser")
    # encontrando as noticias
    tenis = soup.find_all("html", class_="ng-scope")

    print("Air max TN: ")
    for index, noticia in enumerate(tenis):
        print(f"{index + 1}. {noticia.text.strip()} - {noticia['href']} ")

