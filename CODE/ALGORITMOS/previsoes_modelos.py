import pandas as pd
import joblib  # Para carregar o modelo salvo
import os

# Definir caminhos dos arquivos
input_file = "../../FILE/TRATAMENTO/Mapeamento_Filmes_Atualizado.csv"

# Carregar os dados de entrada novamente
df = pd.read_csv(input_file, sep=";")

# Separar os dados
X = df.drop(columns=["Filme", "Oscar"])  # Pegamos todas as colunas menos a de Oscar e Filme

# Lista de algoritmos para processar
algoritmos = ["REGRESSAO_LOGISTICA", "ARVORE_DECISAO", "FLORESTA_ALEATORIA"]

for algoritmo in algoritmos:
    try:
        # Definir caminhos
        modelo_path = f"../../FILE/ALGORITMOS/{algoritmo}/modelo_{algoritmo.lower()}.pkl"
        output_file = f"../../FILE/ALGORITMOS/{algoritmo}/previsoes_{algoritmo.lower()}.csv"

        # Carregar o modelo treinado
        modelo = joblib.load(modelo_path)

        # Fazer previsões
        df["Previsto"] = modelo.predict(X)

        # Converter 1 e 0 para "Vencedor" e "Não Vencedor"
        df["Previsto"] = df["Previsto"].map({1: "Vencedor", 0: "Não Vencedor"})

        # Criar um DataFrame apenas com Filme e Previsão
        resultados = df[["Filme", "Previsto"]]

        # Salvar as previsões em um arquivo CSV
        os.makedirs(f"../../FILE/ALGORITMOS/{algoritmo}", exist_ok=True)
        resultados.to_csv(output_file, index=False, sep=";")

        print(f"✔ Previsões do {algoritmo} salvas em: {output_file}")

    except Exception as e:
        print(f"❌ Erro ao processar {algoritmo}: {e}")
