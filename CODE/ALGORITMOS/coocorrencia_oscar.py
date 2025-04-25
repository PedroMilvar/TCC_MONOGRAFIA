import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Caminhos
input_file = "../../FILE/TRATAMENTO/Mapeamento_Filmes_Atualizado.csv"
output_csv = "../../FILE/ALGORITMOS/coocorrencia_com_oscar.csv"
output_bar = "../../FILE/GRAFICOS/coocorrencia_barra_oscar.png"
output_heatmap = "../../FILE/GRAFICOS/coocorrencia_heatmap_oscar.png"

# Carregar os dados
df = pd.read_csv(input_file, sep=";")

# Selecionar apenas premiações + Oscar
premiacoes = df.drop(columns=["Filme"])
premiacoes_corr = premiacoes.corr(method='pearson')  # ou 'spearman'

# Obter apenas a correlação com o Oscar
correlacoes_com_oscar = premiacoes_corr["Oscar"].drop("Oscar").sort_values(ascending=False)

# Salvar em CSV
correlacoes_com_oscar.to_csv(output_csv, sep=";", header=["Correlacao_com_Oscar"])

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(x=correlacoes_com_oscar.values, y=correlacoes_com_oscar.index, palette="Blues_d")
plt.title("Correlação (Coocorrência) entre Premiações e o Oscar")
plt.xlabel("Correlação com o Oscar")
plt.ylabel("Premiação")
plt.tight_layout()
plt.savefig(output_bar)
plt.close()

# Heatmap
plt.figure(figsize=(9, 1))
sns.heatmap(premiacoes_corr[["Oscar"]].T.drop(columns="Oscar"), annot=True, cmap="Blues", fmt=".2f")
plt.title("Coocorrência com o Oscar (Heatmap)")
plt.tight_layout()
plt.savefig(output_heatmap)
plt.close()

print(f"CSV salvo em: {output_csv}")
print(f"Gráfico de barras salvo em: {output_bar}")
print(f"Heatmap salvo em: {output_heatmap}")
