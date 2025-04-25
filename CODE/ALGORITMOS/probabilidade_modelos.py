import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib  # Para carregar os modelos

# Diretórios de entrada e saída
base_dir = "../../FILE/ALGORITMOS"
modelos = {
    "Regressao_Logistica": {
        "nome_arquivo": "modelo_regressao_logistica.pkl",
        "pasta": "REGRESSAO_LOGISTICA"
    },
    "ARVORE_DECISAO": {
        "nome_arquivo": "modelo_arvore_decisao.pkl",
        "pasta": "ARVORE_DECISAO"
    },
    "FLORESTA_ALEATORIA": {
        "nome_arquivo": "modelo_floresta_aleatoria.pkl",
        "pasta": "FLORESTA_ALEATORIA"
    }
}

# Dados de entrada para previsão (exemplo)
input_file = "../../FILE/TRATAMENTO/Mapeamento_Filmes_Atualizado.csv"
df = pd.read_csv(input_file, sep=';')
X = df.drop(columns=["Filme", "Oscar"])

# Para armazenar as previsões com probabilidade
resultados = []

for nome_modelo, info in modelos.items():
    caminho_modelo = os.path.join(base_dir, info["pasta"], info["nome_arquivo"])
    modelo = joblib.load(caminho_modelo)

    # Obter as probabilidades de previsão (classe 1 = vencedor)
    probabilidades = modelo.predict_proba(X)[:, 1]  # P(class=1)
    previsoes = modelo.predict(X)

    temp = pd.DataFrame({
        "Filme": df["Filme"],
        "Previsao": previsoes,
        "Chance_Vitoria_%": (probabilidades * 100).round(2),
        "Modelo": nome_modelo
    })
    resultados.append(temp)

# Concatenar todas as previsões
df_probabilidades = pd.concat(resultados)

# Salvar como CSV
df_probabilidades.to_csv("../../FILE/ALGORITMOS/probabilidades_modelos.csv", sep=';', index=False)
print("Probabilidades por modelo salvas em: ../../FILE/ALGORITMOS/probabilidades_modelos.csv")
