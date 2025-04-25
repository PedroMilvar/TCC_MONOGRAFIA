import requests
from bs4 import BeautifulSoup
import csv
import os

# URL da página
url = "https://pt.wikipedia.org/wiki/Predefinição:SAG_de_melhor_elenco_em_cinema"

# Pasta para salvar o arquivo
pasta_saida = "FILE"
os.makedirs(pasta_saida, exist_ok=True)
arquivo_saida = os.path.join(pasta_saida, "SAG_Awards_Winners_Formatted.csv")

try:
    # Fazendo a requisição
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
    print("Requisição bem-sucedida!")

    # Criando o objeto BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Selecionando os elementos da lista de vencedores
    tags_ul = soup.select('div[style="padding:0em 0.25em"] ul li')
    print("Itens encontrados:", len(tags_ul))

    vencedores = []

    # Extraindo os dados
    for tag in tags_ul:
        try:
            filme = tag.find('a').get_text(strip=True)  # Nome do filme
            ano = tag.find('span').get_text(strip=True)  # Ano
            ano_numerico = int(ano.strip("()"))  # Remove os parênteses e converte para número
            if ano_numerico >= 2004:  # Filtra apenas os anos de 2004 em diante
                vencedores.append((ano_numerico, "SAG Awards - Melhor Elenco", filme))
        except (AttributeError, ValueError):
            print("Erro ao processar o item:", tag)

    # Salvando os dados no arquivo CSV
    with open(arquivo_saida, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Ano", "Premiação", "Filme"])  # Cabeçalhos das colunas
        writer.writerows(vencedores)

    print(f"Dados salvos em: {arquivo_saida}")
    print("Vencedores extraídos:")
    for ano, premiacao, filme in vencedores:
        print(f"{ano} | {premiacao} | {filme}")

except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")

except Exception as e:
    print(f"Erro inesperado: {e}")
