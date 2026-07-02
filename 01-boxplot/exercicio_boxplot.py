# -*- coding: utf-8 -*-
"""
Exercício Box Plot — Semana 12 (Estatística Aplicada à Análise Preditiva)
Tempo diário (em horas) de uso de smartphone por 15 adolescentes.

Método dos quartis: Tukey, INCLUINDO a mediana nos subgrupos
(conforme a dica do exercício e o slide 33 da aula M1S12).

Para rodar: python exercicio_boxplot.py
Requisito: pip install matplotlib
"""

import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# Passo 0 — Dados brutos e ordenação
# ------------------------------------------------------------------
dados = [5.5, 1.5, 4.5, 2.0, 2.5, 3.0, 3.5, 7.0, 4.0, 4.5, 5.0, 6.0, 6.5, 9.5, 3.0]
dados_ordenados = sorted(dados)
n = len(dados_ordenados)

print("=" * 60)
print("EXERCÍCIO BOX PLOT — Resolução passo a passo")
print("=" * 60)
print(f"\nDados ordenados ({n} valores):")
print(dados_ordenados)

# ------------------------------------------------------------------
# Tarefa 1 — Cinco números resumidos (método de Tukey, N ímpar)
# ------------------------------------------------------------------
minimo = dados_ordenados[0]
maximo = dados_ordenados[-1]

# N = 15 (ímpar): a mediana é o termo central (8ª posição, índice 7)
mediana = dados_ordenados[n // 2]

# Incluindo a mediana em AMBOS os subgrupos (cada um fica com 8 elementos)
grupo_inferior = dados_ordenados[: n // 2 + 1]   # posições 1 a 8
grupo_superior = dados_ordenados[n // 2:]        # posições 8 a 15

# Cada subgrupo tem 8 elementos (par): quartil = média dos 2 centrais
q1 = (grupo_inferior[3] + grupo_inferior[4]) / 2
q3 = (grupo_superior[3] + grupo_superior[4]) / 2

print("\n--- Tarefa 1: Cinco números resumidos ---")
print(f"Grupo inferior (com a mediana): {grupo_inferior}")
print(f"Grupo superior (com a mediana): {grupo_superior}")
print(f"Mínimo  = {minimo}")
print(f"Q1      = {q1}")
print(f"Mediana = {mediana}")
print(f"Q3      = {q3}")
print(f"Máximo  = {maximo}")

# ------------------------------------------------------------------
# Tarefa 2 — Intervalo Interquartil (AIQ / IQR)
# ------------------------------------------------------------------
aiq = q3 - q1
print("\n--- Tarefa 2: Intervalo Interquartil ---")
print(f"AIQ = Q3 - Q1 = {q3} - {q1} = {aiq}")

# ------------------------------------------------------------------
# Tarefa 3 — Limites de Discrepância
# ------------------------------------------------------------------
limite_inferior = q1 - 1.5 * aiq
limite_superior = q3 + 1.5 * aiq
print("\n--- Tarefa 3: Limites de Discrepância ---")
print(f"1,5 x AIQ = {1.5 * aiq}")
print(f"LI = Q1 - 1,5 x AIQ = {q1} - {1.5 * aiq} = {limite_inferior}")
print(f"LS = Q3 + 1,5 x AIQ = {q3} + {1.5 * aiq} = {limite_superior}")

# ------------------------------------------------------------------
# Tarefa 4 — Identificação de outliers
# ------------------------------------------------------------------
outliers = [x for x in dados_ordenados if x < limite_inferior or x > limite_superior]
print("\n--- Tarefa 4: Outliers ---")
if outliers:
    print(f"Outliers encontrados: {outliers}")
else:
    print("Nenhum outlier: todos os valores estão dentro de "
          f"[{limite_inferior}; {limite_superior}].")
    print(f"Obs.: o maior valor ({maximo}) ficou a apenas "
          f"{round(limite_superior - maximo, 3)}h do limite superior!")

# ------------------------------------------------------------------
# Tarefa 5 — Desenhar o Box Plot
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 4))

ax.boxplot(
    dados_ordenados,
    vert=False,               # boxplot horizontal, como no exercício
    widths=0.5,
    patch_artist=True,        # permite colorir a caixa
    boxprops=dict(facecolor="#B5D4F4", edgecolor="#185FA5", linewidth=1.5),
    medianprops=dict(color="#0C447C", linewidth=2.5),
    whiskerprops=dict(color="#185FA5", linewidth=1.5),
    capprops=dict(color="#185FA5", linewidth=1.5),
)

# Anotações dos cinco números no gráfico
for valor, rotulo in [(minimo, "Mín"), (q1, "Q1"), (mediana, "Md"),
                      (q3, "Q3"), (maximo, "Máx")]:
    ax.annotate(f"{rotulo}\n{valor}", xy=(valor, 1.28), ha="center",
                fontsize=9, color="#0C447C")

# Linha do limite superior (tracejada) para mostrar o critério de outlier
ax.axvline(limite_superior, color="#BA7517", linestyle="--", linewidth=1)
ax.annotate(f"LS = {limite_superior}", xy=(limite_superior, 0.62),
            ha="center", fontsize=9, color="#854F0B")

ax.set_xlabel("Tempo de uso do smartphone (horas/dia)")
ax.set_yticks([])
ax.set_title("Box Plot — Tempo diário de smartphone (15 adolescentes)")
ax.set_xlim(0, 10.5)
ax.grid(axis="x", alpha=0.3)

plt.tight_layout()
plt.savefig("boxplot_exercicio.png", dpi=150)   # salva a imagem para o AVA/GitHub
plt.show()

print("\nGráfico salvo como 'boxplot_exercicio.png'.")
