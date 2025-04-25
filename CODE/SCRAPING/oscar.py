import requests
from bs4 import BeautifulSoup
import csv
import os
import re

# Função para realizar o scraping dos vencedores do Oscar de Melhor Filme
def scrape_oscar_winners(url):
    print("Iniciando scraping da URL:", url)

    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
    except Exception as e:
        print(f"Erro ao acessar a URL: {e}")
        return

    print("Requisição bem-sucedida!")
    soup = BeautifulSoup(response.text, 'html.parser')

    # Seleciona o elemento HTML relevante
    award_section = soup.find('div', {'role': 'navigation', 'class': 'navbox', 'aria-labelledby': "Óscar_de_Melhor_Filme"})
    if not award_section:
        print("Seção de premiação não encontrada!")
        return

    # Localiza todas as listas de filmes vencedores
    award_lists = award_section.find_all('div', {'style': 'padding:0em 0.25em'})
    if not award_lists:
        print("Listas de filmes vencedores não encontradas!")
        return

    winners = []

    for award_list in award_lists:
        items = award_list.find_all('li')
        for item in items:
            try:
                # Extrai o nome do filme
                film = item.find('a').get_text(strip=True)
                # Extrai o ano
                year_match = re.search(r'\d{4}', item.get_text(strip=True))
                if year_match:
                    year = int(year_match.group())
                    winners.append({"Ano": year, "Premiação": "Oscar - Melhor Filme", "Filme": film})
            except AttributeError:
                print("Erro ao processar o item:", item)

    # Salva os dados em um arquivo CSV
    folder = "FILE"
    file_name = "Oscar_Best_Picture_Winners.csv"
    file_path = os.path.join(folder, file_name)

    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Ano", "Premiação", "Filme"])
        writer.writeheader()
        writer.writerows(winners)

    print(f"\nVencedores extraídos e salvos em: {file_path}")
    print("Vencedores:")
    for winner in winners:
        print(winner)

# URL da página do Oscar de Melhor Filme
url = "https://pt.wikipedia.org/wiki/Oscar_de_melhor_filme"

# Executa o scraping
scrape_oscar_winners(url)
