import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Carregar os dados de probabilidades
df = pd.read_csv("../../FILE/ALGORITMOS/probabilidades_modelos.csv", sep=';')

# Criar diretório de saída se não existir
grafico_dir = "../../FILE/GRAFICOS/PROBABILIDADES"
os.makedirs(grafico_dir, exist_ok=True)

# 1. Gráfico de Distribuição de Probabilidades
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Chance_Vitoria_%", hue="Modelo", bins=20, kde=True, element="step")
plt.title("Distribuição das Probabilidades de Vitória por Modelo")
plt.xlabel("Chance de Vitória (%)")
plt.ylabel("Quantidade de Filmes")
plt.savefig(f"{grafico_dir}/distribuicao_probabilidades_modelos.png")
plt.close()

# 2. Gráfico dos Top 10 Filmes com Maior Chance por Modelo
top_filmes = df.groupby("Modelo").apply(lambda x: x.nlargest(10, "Chance_Vitoria_%")).reset_index(drop=True)

g = sns.catplot(
    data=top_filmes,
    x="Chance_Vitoria_%", y="Filme",
    col="Modelo", kind="bar",
    height=6, aspect=1
)
g.set_titles("Top 10 - {col_name}")
g.set_xlabels("Chance de Vitória (%)")
g.set_ylabels("Filme")
plt.tight_layout()
plt.savefig(f"{grafico_dir}/top_10_filmes_por_modelo.png")
plt.close()

# 3. Boxplot das Probabilidades
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Modelo", y="Chance_Vitoria_%")
plt.title("Boxplot das Probabilidades de Vitória por Modelo")
plt.ylabel("Chance de Vitória (%)")
plt.xlabel("Modelo")
plt.savefig(f"{grafico_dir}/boxplot_probabilidades_modelos.png")
plt.close()

print(f"Gráficos salvos em: {grafico_dir}")
