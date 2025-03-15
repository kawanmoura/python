from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurar o navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executar em modo headless (sem interface gráfica)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

# Iniciar o navegador
driver = webdriver.Chrome(options=options)

# Acessar a URL da Droper
url = 'https://droper.app/buscar/nike'
driver.get(url)
time.sleep(5)  # Esperar a página carregar

# Verificar se a página foi carregada corretamente
if "Droper" in driver.title:
    print("Página carregada com sucesso")
else:
    print("Falha ao carregar a página")
    driver.quit()
    exit()

# Extrair dados dos produtos
try:
    # Localizar os produtos
    produtos = driver.find_elements(By.CLASS_NAME, 'ck-card-dropv2')
    print(f'Número de produtos encontrados: {len(produtos)}')  # Mensagem de depuração

    for produto in produtos:
        try:
            # Extrair modelo
            modelo = produto.find_element(By.CLASS_NAME, 'ck-link').text
        except:
            modelo = 'Modelo não encontrado'

        try:
            # Extrair preço
            preco = produto.find_element(By.CLASS_NAME, 'pl10').text
        except:
            preco = 'Preço não encontrado'

        # Exibir as informações
        print(f'Modelo: {modelo}')
        print(f'Preço: {preco}')
        print('-' * 50)

except Exception as e:
    print('Erro ao extrair dados:', e)

# Fechar o navegador
driver.quit()