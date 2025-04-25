import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Definição dos diretórios
input_file = "../../FILE/TRATAMENTO/Mapeamento_Filmes_Atualizado.csv"
output_dir = "../../FILE/ALGORITMOS/REGRESSAO_LOGISTICA"
grafico_dir = "../../FILE/GRAFICOS"

# Criar diretórios se não existirem
os.makedirs(output_dir, exist_ok=True)
os.makedirs(grafico_dir, exist_ok=True)

# Carregar os dados
df = pd.read_csv(input_file, sep=";")

# Separar features e target
X = df.drop(columns=["Oscar", "Filme"])
y = df["Oscar"]

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo
modelo = LogisticRegression(max_iter=200)
modelo.fit(X_train, y_train)

# Salvar o modelo treinado
modelo_path = f"{output_dir}/modelo_regressao_logistica.pkl"
with open(modelo_path, "wb") as f:
    pickle.dump(modelo, f)

# Fazer previsões no conjunto de teste
y_pred_test = modelo.predict(X_test)

# Avaliar o modelo no conjunto de teste
accuracy = accuracy_score(y_test, y_pred_test)
report = classification_report(y_test, y_pred_test)
conf_matrix = confusion_matrix(y_test, y_pred_test)

# Salvar resultados do teste
with open(f"{output_dir}/resultados_teste_regressao_logistica.txt", "w") as f:
    f.write(f"Accuracy: {accuracy:.4f}\n")
    f.write("Classification Report:\n")
    f.write(report)
    f.write("\nConfusion Matrix:\n")
    f.write(str(conf_matrix))

# Salvar previsões no conjunto de teste
df_test = df.iloc[X_test.index].copy()
df_test["Previsao_Oscar"] = y_pred_test
df_test[["Filme", "Previsao_Oscar"]].to_csv(f"{output_dir}/previsoes_teste_regressao_logistica.csv", sep=";", index=False)

# Criar matriz de confusão para o conjunto de teste
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["Não Vencedor", "Vencedor"], yticklabels=["Não Vencedor", "Vencedor"])
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.title("Matriz de Confusão - Regressão Logística (Teste)")
plt.savefig(f"{grafico_dir}/matriz_confusao_teste_regressao_logistica.png")
plt.close()

# Fazer previsões em toda a base
modelo.fit(X, y)
df["Previsao_Oscar"] = modelo.predict(X)

# Salvar previsões completas
df[["Filme", "Previsao_Oscar"]].to_csv(f"{output_dir}/previsoes_completas_regressao_logistica.csv", sep=";", index=False)

print(f"Resultados e previsões salvos em {output_dir}, gráficos em {grafico_dir}")
