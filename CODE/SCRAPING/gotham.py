import os
import requests
from bs4 import BeautifulSoup
import csv

# Define a URL da página da Wikipédia
url = 'https://en.wikipedia.org/wiki/Gotham_Independent_Film_Award_for_Best_Feature'

# Realiza a requisição HTTP para obter o conteúdo da página
response = requests.get(url)
response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

# Analisa o conteúdo HTML da página
soup = BeautifulSoup(response.text, 'html.parser')

# Encontra todas as tabelas na página
tables = soup.find_all('table', {'class': 'wikitable'})

# Lista para armazenar os vencedores por ano
winners = []

# Itera sobre as tabelas encontradas
for table in tables:
    # Encontra todas as linhas da tabela
    rows = table.find_all('tr')
    for row in rows:
        # Encontra as células da linha
        cells = row.find_all('td')
        if len(cells) >= 2:
            # Extrai o ano e verifica o vencedor
            year = cells[0].get_text(strip=True)
            # Procura o vencedor em negrito ou itálico
            winner_tag = cells[1].find(['b', 'i'])
            if winner_tag:
                winner = winner_tag.get_text(strip=True)
                # Armazena o resultado como um dicionário
                winners.append({"Ano": year, "Premiação": "Gotham Independent Film Award for Best Feature", "Filme": winner})

# Define o caminho da pasta e do arquivo
folder_name = "FILE"
file_name = "gotham_awards_winners.csv"
file_path = os.path.join(folder_name, file_name)

# Verifica se a pasta FILE existe; se não, cria a pasta
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Escreve os dados em um arquivo CSV dentro da pasta FILE
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Ano", "Premiação", "Filme"])
    writer.writeheader()
    writer.writerows(winners)

print(f"Dados salvos em: {file_path}")
