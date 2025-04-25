import pandas as pd

# Carregar os arquivos
oscar_file = 'Oscar_Best_Picture_Winners.csv'
premiacoes_file = 'premiacoes.csv'

# Leitura dos arquivos
oscar_df = pd.read_csv(oscar_file, sep=';')
premiacoes_df = pd.read_csv(premiacoes_file, sep=';')

print(premiacoes_df.columns)

# Preencher as colunas de premiações no arquivo do Oscar com 0, se ainda não estiverem preenchidas
for premiacao in premiacoes_df['Premiacao'].unique():
    if premiacao not in oscar_df.columns:
        oscar_df[premiacao] = 0

# Comparar os filmes e marcar os vencedores
for index, oscar_row in oscar_df.iterrows():
    oscar_film = oscar_row['Filme']
    oscar_year = oscar_row['Ano']

    # Filtrar os registros das premiações com o mesmo ano e filme
    matched_premiacoes = premiacoes_df[
        (premiacoes_df['Ano'] == oscar_year) & (premiacoes_df['Filme'] == oscar_film)
    ]

    for _, premiacao_row in matched_premiacoes.iterrows():
        premiacao_name = premiacao_row['Premiacao']
        if premiacao_name in oscar_df.columns:
            oscar_df.at[index, premiacao_name] = 1

# Salvar o arquivo atualizado com separador ";"
output_file = 'FILE/Oscar_Best_Picture_Winners_Updated3.csv'
oscar_df.to_csv(output_file, index=False, sep=';')

print(f"Arquivo atualizado salvo em: {output_file}")
