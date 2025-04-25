import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Caminhos dos arquivos
input_file = "../../FILE/TRATAMENTO/Mapeamento_Filmes_Atualizado.csv"
output_dir = "../../FILE/ESTATISTICAS"
grafico_dir = "../../FILE/GRAFICOS"

# Criar diretórios se não existirem
os.makedirs(output_dir, exist_ok=True)
os.makedirs(grafico_dir, exist_ok=True)

# Ler o arquivo
df = pd.read_csv(input_file, sep=';')

# Remover colunas não numéricas
colunas_validas = [col for col in df.columns if col not in ['Filme']]
df_numerico = df[colunas_validas]

# Cálculo de correlação de Pearson
pearson_resultados = []
for col in df_numerico.columns:
    if col != "Oscar":
        corr, _ = stats.pearsonr(df_numerico[col], df_numerico["Oscar"])
        pearson_resultados.append({"Premiação": col, "Correlação_Pearson": round(corr, 4)})

df_pearson = pd.DataFrame(pearson_resultados)
df_pearson.to_csv(f"{output_dir}/Pearson_Correlacao.csv", index=False, sep=';')

# Cálculo de correlação de Spearman
spearman_resultados = []
for col in df_numerico.columns:
    if col != "Oscar":
        corr, _ = stats.spearmanr(df_numerico[col], df_numerico["Oscar"])
        spearman_resultados.append({"Premiação": col, "Correlação_Spearman": round(corr, 4)})

df_spearman = pd.DataFrame(spearman_resultados)
df_spearman.to_csv(f"{output_dir}/Spearman_Correlacao.csv", index=False, sep=';')

# Gráfico Pearson
plt.figure(figsize=(10,6))
sns.barplot(data=df_pearson, x="Correlação_Pearson", y="Premiação", palette="Blues_r")
plt.title("Correlação de Pearson com o Oscar")
plt.xlabel("Coeficiente de Correlação")
plt.ylabel("Premiação")
plt.tight_layout()
plt.savefig(f"{grafico_dir}/correlacao_pearson_oscar.png")
plt.close()

# Gráfico Spearman
plt.figure(figsize=(10,6))
sns.barplot(data=df_spearman, x="Correlação_Spearman", y="Premiação", palette="Greens_r")
plt.title("Correlação de Spearman com o Oscar")
plt.xlabel("Coeficiente de Correlação")
plt.ylabel("Premiação")
plt.tight_layout()
plt.savefig(f"{grafico_dir}/correlacao_spearman_oscar.png")
plt.close()

print("✅ Correlações calculadas e salvas com sucesso!")
