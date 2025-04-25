import pandas as pd
import scipy.stats as stats
import os

# Diretórios
input_file = "../../FILE/TRATAMENTO/Mapeamento_Filmes_Atualizado.csv"
output_dir = "../../FILE/ALGORITMOS/QuiQuadrado"

# Criar diretório de saída se não existir
os.makedirs(output_dir, exist_ok=True)

# Carregar o arquivo atualizado
df = pd.read_csv(input_file, sep=';')

# Definir Oscar como variável de resposta
y = df['Oscar']

# Criar um dicionário para armazenar os resultados
resultados = []

# Aplicar o teste qui-quadrado para cada premiação
for coluna in df.columns:
    if coluna not in ['Filme', 'Oscar']:  # Ignorar a coluna de filmes e a própria variável alvo
        tabela_contingencia = pd.crosstab(df[coluna], y)
        chi2, p, dof, expected = stats.chi2_contingency(tabela_contingencia)

        resultados.append({
            "Premiação": coluna,
            "Qui-Quadrado": round(chi2, 4),
            "P-Valor": round(p, 4)
        })

# Criar um DataFrame com os resultados
df_resultados = pd.DataFrame(resultados)

# Exibir os resultados
print(df_resultados)

# Salvar os resultados em um CSV
output_path = f"{output_dir}/Resultados_QuiQuadrado.csv"
df_resultados.to_csv(output_path, index=False, sep=';')
print(f"Resultados salvos em: {output_path}")
