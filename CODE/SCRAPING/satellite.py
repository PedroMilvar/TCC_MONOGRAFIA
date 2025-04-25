import requests
from bs4 import BeautifulSoup
import csv
import os
import re


def scrape_specific_satellite_awards(url, start_year=2004):
    print("Iniciando scraping da URL:", url)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Erro ao acessar a URL: {e}")
        return

    print("Requisição bem-sucedida!")
    soup = BeautifulSoup(response.text, 'html.parser')

    # Localiza o elemento específico no HTML
    specific_container = soup.find('td', {'class': 'navbox-list', 'style': 'text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px'})
    if not specific_container:
        print("Elemento HTML específico não encontrado!")
        return

    awards = []
    items = specific_container.find_all('li')

    for item in items:
        # Extrair o ano do texto
        match = re.search(r'\((\d{4})\)', item.text)
        if match:
            year = int(match.group(1))
            if year >= start_year:  # Filtrar apenas anos a partir de 2004
                film = item.find('a').text if item.find('a') else item.text.strip()
                awards.append({
                    "Ano": year,
                    "Premiação": "Prêmios Satellite de Melhor Filme",
                    "Filme": film
                })
                print(f"Item extraído: Ano={year}, Filme={film}")

    # Salvar os resultados em um arquivo CSV
    folder = "FILE"
    file_name = "Satellite_Awards_Specific_From_2004.csv"
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
url = "https://pt.wikipedia.org/wiki/Pr%C3%AAmios_Satellite"

# Executar o scraping
scrape_specific_satellite_awards(url, start_year=2004)
