import requests
from bs4 import BeautifulSoup
import csv
import os
import re


def scrape_dga_awards(url, start_year=2004):
    print("Iniciando scraping da URL:", url)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Erro ao acessar a URL: {e}")
        return

    print("Requisição bem-sucedida!")
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra todas as tabelas relevantes na página
    tables = soup.find_all('table', {'class': 'wikitable'})
    if not tables:
        print("Tabelas não encontradas!")
        return

    print(f"{len(tables)} tabelas encontradas!")
    winners = []
    current_year = None

    # Itera sobre cada tabela na página
    for table_index, table in enumerate(tables, start=1):
        print(f"\nProcessando tabela {table_index}...")

        for row_index, row in enumerate(table.find_all('tr'), start=1):
            cells = row.find_all('td')

            # Depuração
            print(f"\nProcessando linha {row_index} da tabela {table_index}...")
            print(f"Células: {[cell.get_text(strip=True) for cell in cells]}")

            # Atualiza o ano se houver
            if len(cells) >= 4:  # Ano + 3 colunas (diretor, filme, referência)
                raw_year = cells[0].get_text(strip=True)
                match = re.search(r'\d{4}', raw_year)
                if match:
                    current_year = int(match.group())
                    print(f"Ano atualizado: {current_year}")

            # Ignora anos fora do intervalo desejado
            if current_year is not None and current_year < start_year:
                print(f"Ano {current_year} ignorado (anterior a {start_year}).")
                continue

            # Verifica se a linha contém um vencedor
            if len(cells) == 4:  # Conferindo se há colunas suficientes
                film = cells[2].get_text(strip=True)
                winners.append({"Ano": current_year, "Premiação": "DGA Awards - Melhor Direção", "Filme": film})
                print(f"Vencedor encontrado: Ano={current_year}, Premiação=DGA Awards - Melhor Direção, Filme={film}")

    # Salva os vencedores em um arquivo CSV
    folder = "FILE"
    file_name = "DGA_Awards_Winners_Formatted.csv"
    file_path = os.path.join(folder, file_name)

    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Ano", "Premiação", "Filme"])
        writer.writeheader()
        writer.writerows(winners)

    print(f"\nVencedores extraídos: {winners}")
    print(f"Dados salvos em: {file_path}")


# URL da página do DGA Awards
url = "https://en.wikipedia.org/wiki/Directors_Guild_of_America_Award_for_Outstanding_Directing_–_Feature_Film"

# Executa o scraping
scrape_dga_awards(url)
