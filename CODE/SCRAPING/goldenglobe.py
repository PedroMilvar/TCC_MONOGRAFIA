import requests
from bs4 import BeautifulSoup
import csv
import os
import re

def scrape_golden_globe_awards(url, start_year=2004):
    print("Iniciando scraping da URL:", url)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Erro ao acessar a URL: {e}")
        return

    print("Requisição bem-sucedida!")
    soup = BeautifulSoup(response.text, 'html.parser')

    # Localizar a seção correta da página
    containers = soup.find_all('td', {'class': 'navbox-list'})
    if not containers:
        print("Seção da tabela não encontrada!")
        return

    awards = []
    for container in containers:
        items = container.find_all('li')
        if not items:
            continue

        for item in items:
            # Extrair o ano do texto
            match = re.search(r'\((\d{4})\)', item.text)
            if match:
                year = int(match.group(1))
                if year >= start_year:  # Filtrar apenas anos a partir de 2004
                    film = item.find('a').text if item.find('a') else item.text.strip()
                    awards.append({
                        "Ano": year,
                        "Premiação": "Globo de Ouro de Melhor Filme de Drama",
                        "Filme": film
                    })
                    print(f"Item extraído: Ano={year}, Filme={film}")

    # Salvar os resultados em um arquivo CSV
    folder = "FILE"
    file_name = "Golden_Globe_Drama_Winners_From_2004.csv"
    file_path = os.path.join(folder, file_name)

    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Ano", "Premiação", "Filme"])
        writer.writeheader()
        writer.writerows(awards)

    print(f"\nVencedores extraídos: {awards}")
    print(f"Dados salvos em: {file_path}")


# URL da página
url = "https://pt.wikipedia.org/wiki/Globo_de_Ouro_de_melhor_filme_dramático"

# Executar o scraping
scrape_golden_globe_awards(url, start_year=2004)
