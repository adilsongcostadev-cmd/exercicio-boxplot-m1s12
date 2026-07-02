# -*- coding: utf-8 -*-
"""
Exercício — Média, Moda e Mediana (dados agrupados)
Tabela 2.4 (Bussab & Morettin): salários dos 36 empregados da Companhia MB.

Para rodar: python exercicio_media_moda_mediana.py
"""

# ------------------------------------------------------------------
# Dados da tabela (limites das classes e frequências)
# ------------------------------------------------------------------
classes = [(4, 8), (8, 12), (12, 16), (16, 20), (20, 24)]
frequencias = [10, 12, 8, 5, 1]
n = sum(frequencias)

# ------------------------------------------------------------------
# Tarefa 1 — Ponto médio (C) e porcentagem acumulada
# ------------------------------------------------------------------
pontos_medios = [(inf + sup) / 2 for inf, sup in classes]
porcentagens = [100 * f / n for f in frequencias]

pct_acumulada = []
acumulado = 0.0
for p in porcentagens:
    acumulado += p
    pct_acumulada.append(acumulado)

print("=" * 72)
print("TAREFA 1 — Tabela com ponto médio (C) e porcentagem acumulada")
print("=" * 72)
print(f"{'Classe':<14}{'ni':>4}{'100fi (%)':>12}{'C (pto médio)':>16}{'% Acum.':>12}")
for (inf, sup), f, pct, c, acum in zip(classes, frequencias, porcentagens,
                                       pontos_medios, pct_acumulada):
    print(f"{inf:>5.2f} |- {sup:<5.2f}{f:>4}{pct:>12.2f}{c:>16.1f}{acum:>12.2f}")
print(f"{'Total':<14}{n:>4}{100.0:>12.2f}")

# ------------------------------------------------------------------
# Tarefa 2 — Média, Moda e Mediana (dados agrupados)
# ------------------------------------------------------------------
print("\n" + "=" * 72)
print("TAREFA 2 — Média, Moda e Mediana")
print("=" * 72)

# MÉDIA: soma ponderada dos pontos médios pelas frequências
parcelas = [f * c for f, c in zip(frequencias, pontos_medios)]
media = sum(parcelas) / n
print("\nMÉDIA (ponderada pelos pontos médios):")
detalhe = " + ".join(f"({f}x{c:g})" for f, c in zip(frequencias, pontos_medios))
print(f"  x̄ = [{detalhe}] / {n}")
print(f"  x̄ = {sum(parcelas):g} / {n} = {media:.2f} salários mínimos")

# MODA: ponto médio da classe de maior frequência (classe modal)
idx_modal = frequencias.index(max(frequencias))
moda = pontos_medios[idx_modal]
print("\nMODA (ponto médio da classe modal):")
print(f"  Classe modal: {classes[idx_modal][0]} |- {classes[idx_modal][1]} "
      f"(ni = {frequencias[idx_modal]})")
print(f"  mo = {moda:g}")

# MEDIANA: com n=36 (par), média da 18ª e 19ª observações.
# Ambas caem na classe cuja frequência acumulada primeiro atinge n/2.
freq_acumulada = []
acum = 0
for f in frequencias:
    acum += f
    freq_acumulada.append(acum)

pos1, pos2 = n // 2, n // 2 + 1          # 18ª e 19ª posições
idx_md = next(i for i, fa in enumerate(freq_acumulada) if fa >= pos1)
mediana = pontos_medios[idx_md]           # ambas na mesma classe -> ponto médio
print("\nMEDIANA (pelos pontos médios):")
print(f"  n = {n} (par) -> média da {pos1}ª e {pos2}ª observações")
print(f"  Freq. acumuladas: {freq_acumulada}")
print(f"  Ambas pertencem à classe {classes[idx_md][0]} |- {classes[idx_md][1]}")
print(f"  md = ({mediana:g} + {mediana:g}) / 2 = {mediana:g}")

# COMPLEMENTO: mediana por interpolação (método do Bussab)
L = classes[idx_md][0]                    # limite inferior da classe mediana
F_ant = freq_acumulada[idx_md - 1] if idx_md > 0 else 0
f_md = frequencias[idx_md]
h = classes[idx_md][1] - classes[idx_md][0]
mediana_interp = L + ((n / 2 - F_ant) / f_md) * h
print("\nCOMPLEMENTO — Mediana por interpolação dentro da classe:")
print(f"  md = {L} + (({n}/2 - {F_ant}) / {f_md}) x {h} = {mediana_interp:.2f}")

# ------------------------------------------------------------------
# Interpretação
# ------------------------------------------------------------------
print("\n" + "=" * 72)
print("INTERPRETAÇÃO")
print("=" * 72)
print(f"Média ({media:.2f}) > Mediana ({mediana:g}) = Moda ({moda:g})")
print("Assimetria positiva: poucos salários altos puxam a média para cima,")
print("enquanto a mediana permanece no centro da distribuição.")
