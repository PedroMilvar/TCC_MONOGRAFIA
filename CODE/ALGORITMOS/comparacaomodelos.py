import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Diretórios de entrada e saída
base_dir = "../../FILE/ALGORITMOS"
modelos = ["REGRESSAO_LOGISTICA", "ARVORE_DECISAO", "FLORESTA_ALEATORIA"]
resultados = {}


def carregar_previsoes(modelo):
    arquivo = f"{base_dir}/{modelo}/previsoes_teste_{modelo.lower()}.csv"
    df = pd.read_csv(arquivo, sep=";")
    return df


# Carregar previsões de cada modelo
dados_modelos = {modelo: carregar_previsoes(modelo) for modelo in modelos}

# Criar um dataframe único para comparação
df_comparacao = dados_modelos["REGRESSAO_LOGISTICA"].copy()
df_comparacao.rename(columns={"Previsao_Oscar": "Regressao_Logistica"}, inplace=True)
for modelo in ["ARVORE_DECISAO", "FLORESTA_ALEATORIA"]:
    df_comparacao[modelo] = dados_modelos[modelo]["Previsao_Oscar"]

# Carregar rótulos reais
y_true = pd.read_csv("../../FILE/TRATAMENTO/Mapeamento_Filmes_Atualizado.csv", sep=";")
y_true = y_true.set_index("Filme")["Oscar"].to_dict()
df_comparacao["Real"] = df_comparacao["Filme"].map(y_true)

# Avaliar cada modelo
for modelo in ["Regressao_Logistica", "ARVORE_DECISAO", "FLORESTA_ALEATORIA"]:
    y_pred = df_comparacao[modelo]
    accuracy = accuracy_score(df_comparacao["Real"], y_pred)
    report = classification_report(df_comparacao["Real"], y_pred, output_dict=True)
    conf_matrix = confusion_matrix(df_comparacao["Real"], y_pred)

    resultados[modelo] = {
        "Acuracia": accuracy,
        "Relatorio": report,
        "Matriz_Confusao": conf_matrix
    }

    # Gerar gráfico da matriz de confusão
    plt.figure(figsize=(6, 4))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["Não Vencedor", "Vencedor"],
                yticklabels=["Não Vencedor", "Vencedor"])
    plt.xlabel("Previsto")
    plt.ylabel("Real")
    plt.title(f"Matriz de Confusão - {modelo}")
    plt.savefig(f"../../FILE/GRAFICOS/matriz_confusao_{modelo}.png")
    plt.close()

# Salvar resultados em CSV
df_comparacao.to_csv("../../FILE/ALGORITMOS/comparacao_modelos.csv", sep=";", index=False)

# Salvar métricas em um arquivo
with open("../../FILE/ALGORITMOS/metricas_modelos.txt", "w") as f:
    for modelo, res in resultados.items():
        f.write(f"Modelo: {modelo}\n")
        f.write(f"Acurácia: {res['Acuracia']:.4f}\n")
        f.write("Relatório de Classificação:\n")
        for classe, metricas in res["Relatorio"].items():
            if isinstance(metricas, dict):
                f.write(f"  Classe {classe}: {metricas}\n")
        f.write(f"Matriz de Confusão:\n{res['Matriz_Confusao']}\n\n")

print("Análise concluída! Resultados salvos em ../../FILE/ALGORITMOS e gráficos em ../../FILE/GRAFICOS")
