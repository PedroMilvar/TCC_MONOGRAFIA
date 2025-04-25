import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Caminhos dos arquivos
modelos = {
    "Regressão Logística": pd.read_csv("C:/Users/pedmi/PycharmProjects/PythonProject/.venv/TCC/FILE/ALGORITMOS/REGRESSAO_LOGISTICA/previsoes_teste_regressao_logistica.csv", sep=';'),
    "Árvore de Decisão": pd.read_csv("C:/Users/pedmi/PycharmProjects/PythonProject/.venv/TCC/FILE/ALGORITMOS/ARVORE_DECISAO/previsoes_teste_arvore_decisao.csv", sep=';'),
    "Floresta Aleatória": pd.read_csv("C:/Users/pedmi/PycharmProjects/PythonProject/.venv/TCC/FILE/ALGORITMOS/FLORESTA_ALEATORIA/previsoes_teste_floresta_aleatoria.csv", sep=';')
}

# Gerar gráfico com as 3 matrizes de confusão
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for ax, (nome_modelo, df) in zip(axes, modelos.items()):
    y_true = df["Oscar"] if "Oscar" in df.columns else df.get("Real", [0]*len(df))  # segurança
    y_pred = df["Previsao_Oscar"]

    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Não Vencedor", "Vencedor"])
    disp.plot(ax=ax, cmap="Blues", colorbar=False)
    ax.set_title(nome_modelo)

plt.suptitle("Matrizes de Confusão dos Modelos", fontsize=16, y=1.05)
plt.tight_layout()
plt.savefig("matrizes_confusao_modelos.png", dpi=300, bbox_inches='tight')
plt.show()
