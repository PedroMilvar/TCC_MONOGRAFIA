import pandas as pd

# Caminhos dos arquivos
mapeamento_file = "FILE/Mapeamento_Filmes.csv"
filmes_premiados_file = "FILE/Filmes_Premiados.csv"

# Carregar os arquivos
mapeamento_df = pd.read_csv(mapeamento_file, sep=";")
filmes_premiados_df = pd.read_csv(filmes_premiados_file, sep=";")

# Garantir que todas as colunas de premiações estejam presentes no arquivo de mapeamento
premiacoes_unicas = filmes_premiados_df["Premiacao"].unique()
for premiacao in premiacoes_unicas:
    if premiacao not in mapeamento_df.columns:
        mapeamento_df[premiacao] = 0  # Inicializa com 0

# Atualizar o mapeamento com os vencedores
for _, row in filmes_premiados_df.iterrows():
    filme = row["Filme"]
    premiacao = row["Premiacao"]

    if filme in mapeamento_df["Filme"].values:
        # Definir 1 na coluna correspondente
        mapeamento_df.loc[mapeamento_df["Filme"] == filme, premiacao] = 1

# Converter todas as colunas de premiações para inteiros
colunas_premiacoes = [col for col in mapeamento_df.columns if col != "Filme"]
mapeamento_df[colunas_premiacoes] = mapeamento_df[colunas_premiacoes].fillna(0).astype(int)

# Salvar o arquivo atualizado
output_file = "FILE/Mapeamento_Filmes_Atualizado.csv"
mapeamento_df.to_csv(output_file, index=False, sep=";")

print(f"Arquivo atualizado salvo em: {output_file}")
