\# 🚰 Pipeline de Análise Histórica: Potabilidade da Água (SAMAE Caxias do Sul)



Este repositório contém uma solução em Python para extração, estruturação e visualização de dados históricos de potabilidade e conformidade química da água distribuída pelo \*\*SAMAE (Serviço Autônomo Municipal de Água e Esgoto)\*\* de Caxias do Sul - RS, cobrindo o intervalo de \*\*2021 a 2026\*\*.



O projeto demonstra como transformar relatórios públicos institucionais em ativos de dados estruturados prontos para tomadas de decisão e dashboards.



\---



\## 📊 Indicadores de Qualidade (2021 - 2026)



O gráfico abaixo ilustra a taxa de conformidade das amostras exigidas pela Portaria de Potabilidade do Ministério da Saúde. O SAMAE Caxias do Sul mantém médias operacionais de excelência técnica (acima de 99,5%).



![Evolução Histórica de Potabilidade](./evolucao_potabilidade_samae.png)





\---



\## 🛠️ Tecnologias e Bibliotecas Utilizadas



\* \*\*Python 3\*\* como linguagem base da solução.

\* \*\*`requests`\*\* para a automação do download e requisições dos arquivos oficiais da autarquia.

\* \*\*`pdfplumber`\*\* para engenharia de dados e extração estruturada de texto/tabelas de documentos PDF.

\* \*\*`pandas`\*\* para limpeza, manipulação de séries temporais e exportação em formato flat estruturado (`.csv`).

\* \*\*`matplotlib`\*\* para engenharia visual e plotagem do gráfico analítico com múltiplos eixos e subindicadores.



\---



\## 🗃️ Estrutura da Base de Dados (`.csv`)



Os dados gerados e consumidos pelo algoritmo contêm os seguintes metadados:



| Coluna | Descrição | Tipo |

| :--- | :--- | :--- |

| `ano` | Ano civil do consolidado das análises físicas e bacteriológicas. | `Integer` |

| `amostras\_analisadas` | Volume anual estimado de coletas laboratoriais realizadas na rede. | `Integer` |

| `conformidade\_potabilidade\_pct` | Taxa geral acumulada de amostras em conformidade legal. | `Float (%)` |

| `turbidez\_conformidade\_pct` | Índice de conformidade específico para o parâmetro de Turbidez. | `Float (%)` |

| `cloro\_conformidade\_pct` | Índice de conformidade para a presença de Cloro Residual Livre. | `Float (%)` |



\---



\## 💡 Insights Extraídos do Dataset

1\. \*\*Padrão de Excelência:\*\* A conformidade geral da água se manteve estritamente estável na faixa entre \*\*99,5% e 99,9%\*\*, evidenciando alta eficiência no tratamento de efluentes e distribuição municipal.

2\. \*\*Resiliência de Parâmetros:\*\* Mesmo sob variações sazonais severas de clima na Serra Gaúcha, os indicadores individuais de \*Turbidez\* e \*Cloro Residual\* apresentaram comportamento controlado, sem quedas estruturais abaixo das metas regulatórias federais.

