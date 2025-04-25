import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Criar a figura e os eixos
fig, ax = plt.subplots(figsize=(6, 5))

# Adicionar retângulos
cores = {
    'TP': '#a8e6a1',  # verde claro
    'FP': '#f7a8a8',  # vermelho claro
    'FN': '#f7a8a8',
    'TN': '#a8e6a1'
}

# Posição dos quadrantes: (x, y)
ax.add_patch(patches.Rectangle((0, 1), 1, 1, edgecolor='black', facecolor=cores['TP']))
ax.text(0.5, 1.5, 'Verdadeiro Positivo\n(TP)', ha='center', va='center', fontsize=10)

ax.add_patch(patches.Rectangle((1, 1), 1, 1, edgecolor='black', facecolor=cores['FP']))
ax.text(1.5, 1.5, 'Falso Positivo\n(FP)', ha='center', va='center', fontsize=10)

ax.add_patch(patches.Rectangle((0, 0), 1, 1, edgecolor='black', facecolor=cores['FN']))
ax.text(0.5, 0.5, 'Falso Negativo\n(FN)', ha='center', va='center', fontsize=10)

ax.add_patch(patches.Rectangle((1, 0), 1, 1, edgecolor='black', facecolor=cores['TN']))
ax.text(1.5, 0.5, 'Verdadeiro Negativo\n(TN)', ha='center', va='center', fontsize=10)

# Títulos dos eixos
ax.text(0.5, 2.1, 'Valor Previsto', ha='center', fontsize=12)
ax.text(-0.6, 1.5, 'Positivo', va='center', rotation=90, fontsize=10)
ax.text(-0.6, 0.5, 'Negativo', va='center', rotation=90, fontsize=10)
ax.text(-1.2, 1, 'Valor Real', va='center', rotation=90, fontsize=12)

ax.text(0.5, -0.3, 'Positivo', ha='center', fontsize=10)
ax.text(1.5, -0.3, 'Negativo', ha='center', fontsize=10)

# Ajustar limites e remover eixos
ax.set_xlim(-1, 2.2)
ax.set_ylim(-0.5, 2.2)
ax.axis('off')

plt.tight_layout()
plt.savefig('../../FILE/GRAFICOS/matriz_confusao_exemplo.png', dpi=300)
plt.show()
