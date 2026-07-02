# Exercício 02 — Média, Moda e Mediana (dados agrupados)

Resolução do exercício de medidas de posição central com dados agrupados em classes, baseado na Tabela 2.4 de Bussab & Morettin: distribuição de frequências dos salários dos 36 empregados da seção de orçamentos da Companhia MB.

## 📊 O problema

Dada a tabela de frequências por faixa de salários:

| Classe de salários | Frequência nᵢ | Porcentagem 100fᵢ |
|---|---|---|
| 4,00 ⊢ 8,00 | 10 | 27,78 |
| 8,00 ⊢ 12,00 | 12 | 33,33 |
| 12,00 ⊢ 16,00 | 8 | 22,22 |
| 16,00 ⊢ 20,00 | 5 | 13,89 |
| 20,00 ⊢ 24,00 | 1 | 2,78 |
| **Total** | **36** | **100,00** |

1. Criar a coluna de ponto médio (C) de cada classe e a coluna de porcentagem acumulada;
2. Calcular a média, a moda e a mediana dos dados agrupados com base nos pontos médios e nas frequências.

## ✅ Resultados

| Medida | Valor |
|---|---|
| Média | 11,22 salários mínimos |
| Moda | 10 (ponto médio da classe modal 8 ⊢ 12) |
| Mediana | 10 (pelos pontos médios) / 10,67 (por interpolação) |

**Interpretação:** média (11,22) > mediana (10) = moda (10), caracterizando assimetria positiva — poucos salários altos puxam a média para cima, enquanto a mediana permanece no centro da distribuição. Padrão típico de dados salariais.

## 🚀 Como executar

```bash
python exercicio_media_moda_mediana.py
```

O script imprime a tabela completa da Tarefa 1 e todos os cálculos da Tarefa 2 passo a passo, incluindo a mediana por interpolação como complemento.

## 📚 Referência

- BUSSAB, W. O.; MORETTIN, P. A. *Estatística Básica* (Tabela 2.4).
