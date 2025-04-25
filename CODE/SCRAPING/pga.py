import requests
from bs4 import BeautifulSoup
import csv
import os
import re


def scrape_pga_awards(url):
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
    container = soup.find('td', {'class': 'navbox-list'})
    if not container:
        print("Seção da tabela não encontrada!")
        return

    # Encontrar todas as listas de prêmios
    items = container.find_all('li')
    if not items:
        print("Itens da lista não encontrados!")
        return

    print(f"{len(items)} itens encontrados!")
    awards = []

    for item in items:
        # Extrair o ano do texto
        match = re.search(r'\((\d{4})\)', item.text)
        if match:
            year = match.group(1)
            film = item.find('a').text
            awards.append({"Ano": year, "Premiação": "Producers Guild of America de Melhor Filme", "Filme": film})
            print(f"Item extraído: Ano={year}, Filme={film}")

    # Salvar os resultados em um arquivo CSV
    folder = "FILE"
    file_name = "PGA_Awards_Winners.csv"
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
url = "https://pt.wikipedia.org/wiki/Predefinição:Producers_Guild_of_America_de_melhor_filme"

# Executar o scraping
scrape_pga_awards(url)
