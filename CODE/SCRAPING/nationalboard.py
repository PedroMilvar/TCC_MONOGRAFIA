import os
import requests
from bs4 import BeautifulSoup
import csv


def save_award_winners(url, award_name, start_year=2004):
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
                # Extrai o ano e verifica se está dentro do intervalo
                year_text = cells[0].get_text(strip=True)
                try:
                    year = int(year_text)  # Converte o texto do ano para inteiro
                except ValueError:
                    continue  # Ignora linhas que não contêm anos válidos

                if year >= start_year:  # Filtra apenas anos >= 2004
                    # Procura o vencedor em negrito ou itálico
                    winner_tag = cells[1].find(['b', 'i'])
                    winner = winner_tag.get_text(strip=True) if winner_tag else cells[1].get_text(strip=True)
                    # Adiciona ao dicionário
                    winners.append({"Ano": year, "Premiação": award_name, "Filme": winner})

    # Define o nome do arquivo baseado na premiação
    file_name = f"{award_name.replace(' ', '_')}.csv"
    folder_name = "FILE"
    file_path = os.path.join(folder_name, file_name)

    # Verifica se a pasta FILE existe; se não, cria a pasta
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Salva os dados no arquivo CSV
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Ano", "Premiação", "Filme"])
        writer.writeheader()
        writer.writerows(winners)

    print(f"Dados de {award_name} salvos em: {file_path}")


# Executa o scraping para a premiação "National Board of Review Award for Best Film" de 2004 em diante
save_award_winners(
    url="https://en.wikipedia.org/wiki/National_Board_of_Review_Award_for_Best_Film",
    award_name="National Board of Review Award for Best Film",
    start_year=2004
)
