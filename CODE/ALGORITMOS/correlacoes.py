import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo atualizado
file_path = "../../FILE/TRATAMENTO/Mapeamento_Filmes_Atualizado.csv"  # Substitua pelo caminho correto se necessário
df = pd.read_csv(file_path, sep=";")

# Garantir que os valores sejam inteiros
df.iloc[:, 1:] = df.iloc[:, 1:].astype(int)

# Cálculo de correlação de Spearman
spearman_corr = df.iloc[:, 1:].corr(method="spearman")

# Cálculo de correlação de Pearson
pearson_corr = df.iloc[:, 1:].corr(method="pearson")

# Exibir as matrizes de correlação
print("\nMatriz de Correlação - Spearman:")
print(spearman_corr)

print("\nMatriz de Correlação - Pearson:")
print(pearson_corr)

# Salvar em CSV
spearman_corr.to_csv("Spearman_Correlacao.csv", sep=";")
pearson_corr.to_csv("Pearson_Correlacao.csv", sep=";")

# Plotar a matriz de correlação de Spearman
plt.figure(figsize=(10, 8))
sns.heatmap(spearman_corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matriz de Correlação - Spearman")
plt.show()

# Plotar a matriz de correlação de Pearson
plt.figure(figsize=(10, 8))
sns.heatmap(pearson_corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matriz de Correlação - Pearson")
plt.show()
