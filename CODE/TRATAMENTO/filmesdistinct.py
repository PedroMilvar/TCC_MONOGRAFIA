import pandas as pd

# Carregar o arquivo CSV
file_path = 'premiacoes.csv'  # Insira o caminho correto para o arquivo
df = pd.read_csv(file_path, sep=';')  # Ajuste o separador se necessário

# Extrair filmes distintos
filmes_distintos = df['Filme'].drop_duplicates()

# Criar um novo DataFrame com os filmes distintos
filmes_df = pd.DataFrame({'Filme': filmes_distintos})

# Salvar o resultado em um novo arquivo CSV
output_path = 'filmes_distintos.csv'  # Caminho para salvar o novo arquivo
filmes_df.to_csv(output_path, index=False, sep=';')

print(f"Arquivo com filmes distintos salvo em: {output_path}")
