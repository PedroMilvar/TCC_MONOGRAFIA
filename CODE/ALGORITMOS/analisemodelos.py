import pandas as pd

# Definição do caminho dos arquivos
regressao_file = "../../FILE/ALGORITMOS/REGRESSAO_LOGISTICA/previsoes_completas_regressao_logistica.csv"
arvore_file = "../../FILE/ALGORITMOS/ARVORE_DECISAO/previsoes_completas_arvore_decisao.csv"
floresta_file = "../../FILE/ALGORITMOS/FLORESTA_ALEATORIA/previsoes_completas_floresta_aleatoria.csv"

# Carregar os resultados das previsões completas de cada modelo
regressao = pd.read_csv(regressao_file, sep=";")
arvore = pd.read_csv(arvore_file, sep=";")
floresta = pd.read_csv(floresta_file, sep=";")

# Renomear colunas para identificar modelo
regressao.rename(columns={"Previsao_Oscar": "Regressao_Logistica"}, inplace=True)
arvore.rename(columns={"Previsao_Oscar": "Arvore_Decisao"}, inplace=True)
floresta.rename(columns={"Previsao_Oscar": "Floresta_Aleatoria"}, inplace=True)

# Unir os dados em um único DataFrame para facilitar análise
comparacao_df = regressao.merge(arvore, on="Filme").merge(floresta, on="Filme")

# Contagem total de previsões positivas (1) por modelo
positivos_por_modelo = comparacao_df[["Regressao_Logistica", "Arvore_Decisao", "Floresta_Aleatoria"]].sum()

# Verificar quantos filmes foram previstos como vencedores por todos os modelos
comparacao_df["Todos_Modelos_Previram_Vencedor"] = (
    (comparacao_df["Regressao_Logistica"] == 1) &
    (comparacao_df["Arvore_Decisao"] == 1) &
    (comparacao_df["Floresta_Aleatoria"] == 1)
)

todos_modelos_vencedores = comparacao_df["Todos_Modelos_Previram_Vencedor"].sum()

# Verificar onde todos os modelos erraram (todos 0)
comparacao_df["Todos_Modelos_Previram_Perda"] = (
    (comparacao_df["Regressao_Logistica"] == 0) &
    (comparacao_df["Arvore_Decisao"] == 0) &
    (comparacao_df["Floresta_Aleatoria"] == 0)
)

todos_modelos_derrota = comparacao_df["Todos_Modelos_Previram_Perda"].sum()

# Salvar análise em CSV
output_file = "../../FILE/ALGORITMOS/Analise_Modelos.csv"
comparacao_df.to_csv(output_file, sep=";", index=False)

# Exibir resultados no terminal
print("Quantidade de previsões positivas por modelo:")
print(positivos_por_modelo)
print(f"\nFilmes onde todos os modelos previram como vencedores: {todos_modelos_vencedores}")
print(f"Filmes onde todos os modelos erraram e previram como não vencedores: {todos_modelos_derrota}")

print(f"\nAnálise completa salva em {output_file}")
