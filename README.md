# Exercício Box Plot — Estatística Aplicada à Análise Preditiva

Resolução do exercício de Box Plot da **Semana 12** do curso **Desenvolvimento de IA para Análise Preditiva** (Programa SCTEC / SENAI-SC — Carreira Tech, Etapa Profissionalizar).

## 📊 O problema

Um pesquisador coletou o tempo diário (em horas) que um grupo de 15 adolescentes passa utilizando o smartphone:

```
5.5, 1.5, 4.5, 2.0, 2.5, 3.0, 3.5, 7.0, 4.0, 4.5, 5.0, 6.0, 6.5, 9.5, 3.0
```

Tarefas propostas:

1. Determinar os cinco números resumidos (Mínimo, Q1, Mediana, Q3, Máximo);
2. Calcular o Intervalo Interquartil (AIQ = Q3 − Q1);
3. Calcular os Limites de Discrepância (LI = Q1 − 1,5×AIQ e LS = Q3 + 1,5×AIQ);
4. Identificar possíveis outliers;
5. Desenhar o Box Plot correspondente.

## ✅ Resultados

| Medida | Valor |
|---|---|
| Mínimo | 1.5 h |
| Q1 | 3.0 h |
| Mediana (Q2) | 4.5 h |
| Q3 | 5.75 h |
| Máximo | 9.5 h |
| AIQ | 2.75 |
| Limite Inferior | −1.125 |
| Limite Superior | 9.875 |
| Outliers | Nenhum |

**Método utilizado:** quartis calculados pelo método de Tukey, incluindo a mediana nos subgrupos (N = 15, ímpar).

**Interpretação:** metade dos adolescentes usa o smartphone até 4,5 h/dia e os 50% centrais concentram-se entre 3,0 e 5,75 h. O bigode direito mais longo indica assimetria positiva (cauda à direita). O valor 9,5 h aproxima-se do limite superior (9,875), mas não é classificado como outlier pelo critério de 1,5 × AIQ.

## 🚀 Como executar

1. Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

2. Instale a dependência:

```bash
pip install matplotlib
```

3. Execute o script:

```bash
python exercicio_boxplot.py
```

O script imprime a resolução passo a passo no terminal, exibe o gráfico e salva a imagem `boxplot_exercicio.png`.

## 🛠️ Tecnologias

- Python 3.x
- Matplotlib

## 📚 Referências

- BUSSAB, W. O.; MORETTIN, P. A. *Estatística Básica*.
- MAGALHÃES, M. N.; LIMA, A. C. P. *Noções de Probabilidade e Estatística* (2015).

## 📄 Licença

Material desenvolvido para fins educacionais no âmbito do Programa SCTEC.
