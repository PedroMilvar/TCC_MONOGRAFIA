import requests
from bs4 import BeautifulSoup
import csv
import os


def save_bafta_best_film_winners(url, start_year=2004):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    winners_section = soup.find('div', {'role': 'navigation', 'aria-labelledby': 'BAFTA_Award_for_Best_Film'})

    if not winners_section:
        return

    winners_list = winners_section.find_all('li')
    if not winners_list:
        return

    winners = []
    for li in winners_list:
        text = li.get_text(strip=True)
        if "(" in text and ")" in text:
            try:
                year = int(text.split("(")[-1].replace(")", ""))
                if year >= start_year:
                    film = text.split("(")[0].strip()
                    winners.append({"Ano": year, "Premiação": "BAFTA Award for Best Film", "Filme": film})
            except ValueError:
                continue

    folder_name = "FILE"
    file_name = "BAFTA_Award_for_Best_Film.csv"
    file_path = os.path.join(folder_name, file_name)

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Ano", "Premiação", "Filme"])
        writer.writeheader()
        writer.writerows(winners)


url = "https://en.wikipedia.org/wiki/BAFTA_Award_for_Best_Film"
save_bafta_best_film_winners(url)
