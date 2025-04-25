import pandas as pd

# Arquivos de entrada
oscar_file = 'Oscar_Best_Picture_Winners.csv'
premiacoes_file = 'premiacoes.csv'

# Leitura dos arquivos
oscar_df = pd.read_csv(oscar_file, sep=';')
premiacoes_df = pd.read_csv(premiacoes_file, sep=';')

# Garantir que as colunas de premiações estejam presentes no arquivo do Oscar
for premiacao in premiacoes_df['Premiacao'].unique():
    if premiacao not in oscar_df.columns:
        oscar_df[premiacao] = 0  # Inicializar com 0

# Atualizar o arquivo do Oscar com base no arquivo de premiações
for _, premiacao_row in premiacoes_df.iterrows():
    premiacao = premiacao_row['Premiacao']
    filme = premiacao_row['Filme']

    # Encontrar linhas no arquivo do Oscar com o mesmo filme
    matched_rows = oscar_df[oscar_df['Filme'] == filme]

    if not matched_rows.empty:
        # Atualizar a coluna correspondente à premiação para '1'
        for index in matched_rows.index:
            oscar_df.at[index, premiacao] = 1

# Garantir que todos os valores sejam inteiros (0 ou 1)
oscar_df = oscar_df.fillna(0).astype({col: 'int64' for col in oscar_df.columns if col not in ['Ano', 'Premiacao', 'Filme']})

# Salvar o arquivo atualizado com separador ";"
output_file = 'FILE/Oscar_Best_Picture_Winners_Updated2.csv'
oscar_df.to_csv(output_file, index=False, sep=';')

print(f"Arquivo atualizado salvo em: {output_file}")
