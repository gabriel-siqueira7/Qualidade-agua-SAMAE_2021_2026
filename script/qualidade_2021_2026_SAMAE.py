

# Gráfico simples de evolução histórica de conformidade de potabilidade (2021 - 2026) - SAMAE Caxias do Sul
# Arquivo CSV baixado do site oficial do SAMAE Caxias do Sul e limpo para análise.

import matplotlib.pyplot as plt
import pandas as pd

# 1. Carrega a base de dados .CSV
df = pd.read_csv(r'C:\Users\gasiq\Documents\DocumentosProjetos-Programacao-github\Qualidade-da-água 2021_2026_SAMAE\cleaned\historico_potabilidade_samae_2021_2026.csv', sep=';')

# 2. Inicializa a figura
plt.figure(figsize=(11, 6), dpi=300)

# 3. Plota as séries temporais (Geral, Turbidez e Cloro Activo)
plt.plot(df["ano"], df["conformidade_potabilidade_pct"], label="Conformidade Geral", marker='o', linewidth=3, color='#005b96')
plt.plot(df["ano"], df["turbidez_conformidade_pct"], label="Parâmetro: Turbidez", marker='s', linestyle='--', linewidth=1.5, color='#ff9900')
plt.plot(df["ano"], df["cloro_conformidade_pct"], label="Parâmetro: Cloro Residual", marker='^', linestyle='--', linewidth=1.5, color='#107c10')

# 4. Customização Estética
plt.title("Evolução Histórica de Conformidade de Potabilidade (2021-2026)\nSAMAE Caxias do Sul - RS", fontsize=14, fontweight='bold', pad=20, color='#333333')
plt.xlabel("Ano de Análise", fontsize=11, fontweight='semibold', labelpad=12)
plt.ylabel("Amostras em Conformidade (%)", fontsize=11, fontweight='semibold', labelpad=10)
plt.ylim(99.0, 100.1)

# Alterna a posição vertical dos rótulos de texto
for idx, (x, y) in enumerate(zip(df["ano"], df["conformidade_potabilidade_pct"])):
    if idx % 2 == 0:
        plt.text(x, y + 0.02, f"{y}%", ha='center', va='bottom', fontsize=9, fontweight='bold', color='#005b96')
    else:
        plt.text(x, y - 0.05, f"{y}%", ha='center', va='top', fontsize=9, fontweight='bold', color='#005b96')

# Grade sutil de fundo e posicionamento estratégico da legenda
plt.grid(True, linestyle=':', alpha=0.6, color='#999999')
plt.legend(loc='lower left', frameon=True, facecolor='#ffffff', edgecolor='#cccccc', fontsize=10)

# Inclusão da fonte de dados
plt.text(0.0, -0.22, "Fonte: SAMAE Caxias do Sul - Relatórios de Análises da Água 2021-2026", 
         transform=plt.gca().transAxes, ha='left', va='bottom', 
         fontsize=9, color='#555555', fontweight='semibold')

plt.text(1.0, -0.22, "Autor: Gabriel Siqueira dos Santos", 
         transform=plt.gca().transAxes, ha='right', va='bottom', 
         fontsize=9, color='#555555', fontweight='semibold')

plt.subplots_adjust(bottom=0.18) 

# Salva o gráfico
plt.savefig(r'C:\Users\gasiq\Documents\DocumentosProjetos-Programacao-github\Qualidade-da-água 2021_2026_SAMAE\evolucao_potabilidade_samae.png', dpi=300, bbox_inches='tight')
print("Gráfico exportado com sucesso direto na raiz do projeto!")
