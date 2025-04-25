import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminhos de entrada/saída
input_file = "../../FILE/TRATAMENTO/Mapeamento_Filmes_Atualizado.csv"
output_csv = "../../FILE/ALGORITMOS/coocorrencia_premiacoes.csv"
output_grafico = "../../FILE/GRAFICOS/coocorrencia_premiacoes.png"

# Carregar os dados
df = pd.read_csv(input_file, sep=";")

# Seleciona apenas colunas de premiações (exceto 'Filme')
premiacoes = df.drop(columns=["Filme"])

# Dicionário para guardar taxa de coocorrência com o Oscar
coocorrencia = {}

# Calcular coocorrência entre cada premiação e o Oscar
for premiacao in premiacoes.columns:
    if premiacao != "Oscar":
        # Número de vezes que ambos (premiação e Oscar) são 1
        ambos_1 = ((premiacoes[premiacao] == 1) & (premiacoes["Oscar"] == 1)).sum()
        total_vitorias = premiacoes[premiacao].sum()

        if total_vitorias > 0:
            taxa = ambos_1 / total_vitorias
        else:
            taxa = 0

        coocorrencia[premiacao] = round(taxa, 2)

# Transformar em DataFrame
cooc_df = pd.DataFrame.from_dict(coocorrencia, orient="index", columns=["Taxa de Coocorrência com Oscar"])
cooc_df = cooc_df.sort_values(by="Taxa de Coocorrência com Oscar", ascending=False)

# Salvar CSV
cooc_df.to_csv(output_csv, sep=";")

# Gráfico de barras com os valores ao lado
plt.figure(figsize=(10, 6))
ax = sns.barplot(
    x=cooc_df["Taxa de Coocorrência com Oscar"],
    y=cooc_df.index,
    palette="Blues_d"
)

# Adicionar os valores ao lado de cada barra
for i, (valor, nome) in enumerate(zip(cooc_df["Taxa de Coocorrência com Oscar"], cooc_df.index)):
    ax.text(valor + 0.01, i, f"{valor:.2f}", va="center")

plt.xlabel("Taxa de Coocorrência com o Oscar")
plt.ylabel("Premiação")
plt.title("Coocorrência entre Premiações e o Oscar")
plt.xlim(0, 1.05)  # Deixa espaço para o texto não cortar
plt.tight_layout()
plt.savefig(output_grafico)
plt.close()


print(f"✅ CSV salvo em: {output_csv}")
print(f"✅ Gráfico salvo em: {output_grafico}")
