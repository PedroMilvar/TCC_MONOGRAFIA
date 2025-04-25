import pandas as pd
import os

# Caminhos conforme estrutura
input_file = "../../FILE/ALGORITMOS/Analise_Modelos.csv"
output_dir = "../../FILE/ALGORITMOS/ANALISE_MODELOS"
os.makedirs(output_dir, exist_ok=True)

# Carregar a análise comparativa
df = pd.read_csv(input_file, sep=";")

# Contar previsões positivas por modelo
resumo_modelos = {
    "Regressao_Logistica": df["Regressao_Logistica"].sum(),
    "Arvore_Decisao": df["Arvore_Decisao"].sum(),
    "Floresta_Aleatoria": df["Floresta_Aleatoria"].sum()
}

# Filmes onde todos os modelos previram vitória
todos_acertaram = df[
    (df["Regressao_Logistica"] == 1) &
    (df["Arvore_Decisao"] == 1) &
    (df["Floresta_Aleatoria"] == 1)
]

# Filmes onde todos os modelos previram derrota
todos_erraram = df[
    (df["Regressao_Logistica"] == 0) &
    (df["Arvore_Decisao"] == 0) &
    (df["Floresta_Aleatoria"] == 0)
]

# Discrepâncias entre os modelos
discrepancias = df[
    (df["Regressao_Logistica"] != df["Arvore_Decisao"]) |
    (df["Regressao_Logistica"] != df["Floresta_Aleatoria"]) |
    (df["Arvore_Decisao"] != df["Floresta_Aleatoria"])
]

# Mostrar resumo
print("🔢 Total de previsões positivas:")
for modelo, total in resumo_modelos.items():
    print(f"  - {modelo}: {total}")

print(f"\n✅ Filmes em que todos previram vitória: {len(todos_acertaram)}")
print(f"❌ Filmes em que todos previram derrota: {len(todos_erraram)}")
print(f"⚠️ Filmes com divergência entre modelos: {len(discrepancias)}")

# Salvar arquivos
todos_acertaram.to_csv(f"{output_dir}/filmes_todos_acertaram.csv", sep=";", index=False)
todos_erraram.to_csv(f"{output_dir}/filmes_todos_erraram.csv", sep=";", index=False)
discrepancias.to_csv(f"{output_dir}/filmes_com_divergencias.csv", sep=";", index=False)
