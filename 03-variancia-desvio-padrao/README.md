# Exercício 03 — Variância e Desvio Padrão

Resolução da atividade prática de medidas de dispersão: cálculo da variância e do desvio padrão das notas obtidas por 5 grupos (A, B, C, D, E), todos com a mesma média.

## 📊 O problema

Cinco grupos obtiveram as seguintes notas:

| Grupo | Notas | Característica |
|---|---|---|
| A | 3, 4, 5, 6, 7 | Regular / Moderado |
| B | 1, 3, 5, 7, 9 | Extremo / Disperso |
| C | 5, 5, 5, 5, 5 | Perfeitamente Homogêneo |
| D | 3, 5, 5, 7 | Concentrado no Centro |
| E | 3, 5, 5, 6, 6 | Assimétrico |

Calcular a **variância** e o **desvio padrão** das notas de cada grupo.

## 🧮 Método

Foi utilizada a **variância populacional** (divisão por N), conforme apresentado em aula:

1. Calcular a média do grupo;
2. Calcular o desvio de cada nota em relação à média (xᵢ − x̄);
3. Elevar cada desvio ao quadrado — etapa que resolve o "paradoxo" da soma dos desvios sempre resultar em zero;
4. Variância = média dos desvios ao quadrado;
5. Desvio padrão = raiz quadrada da variância, devolvendo a medida à unidade original dos dados.

## ✅ Resultados

| Grupo | Média | Variância σ² | Desvio Padrão σ |
|---|---|---|---|
| A | 5 | 2,0 | 1,41 |
| B | 5 | 8,0 | 2,83 |
| C | 5 | 0 | 0 |
| D | 5 | 2,0 | 1,41 |
| E | 5 | 1,2 | 1,10 |

## 💡 Interpretação

Todos os grupos possuem **média 5**, mas comportamentos completamente distintos — a demonstração clássica de que a média, sozinha, não descreve um conjunto de dados:

- **Grupo C (σ = 0)**: dispersão nula — todas as notas são iguais à média. Único caso em que a média conta a história completa.
- **Grupo B (σ ≈ 2,83)**: o mais heterogêneo, com notas espalhadas de 1 a 9.
- **Grupos A e D (σ ≈ 1,41)**: mesma dispersão obtida com quantidades de notas (5 e 4) e configurações diferentes — a variância resume um padrão de dispersão, não a "forma" dos dados.
- **Grupo E (σ ≈ 1,10)**: o menos disperso entre os heterogêneos, com desvios assimétricos em torno da média — dispersão e assimetria são características independentes.

**Ranking de homogeneidade:** C > E > A = D > B

## 🚀 Como executar

```bash
python exercicio_variancia_desvio_padrao.py
```

O script imprime, para cada grupo, a resolução completa (média, desvios, desvios ao quadrado, variância e desvio padrão), a tabela-resumo e a interpretação dos resultados.

**Nota técnica:** o script utiliza a variância populacional (÷N). Funções como `statistics.variance()` e `pandas.DataFrame.var()` utilizam por padrão a variância amostral (÷n−1) e produzirão valores diferentes; o equivalente à fórmula da aula é `statistics.pvariance()`.

## 📚 Referência

- BUSSAB, W. O.; MORETTIN, P. A. *Estatística Básica*.