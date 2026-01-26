meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_ano = vendas_1sem + vendas_2sem
mais_vendido = max(vendas_ano)
menos_vendido = min(vendas_ano)
i = vendas_ano.index(mais_vendido)
produto_mais_vendido = vendas_ano[i]
print(produto_mais_vendido)

i = vendas_ano.index(menos_vendido)
produto_menos_vendido = vendas_ano[i]
print(produto_menos_vendido)

i_mais_vendido = vendas_ano.index(mais_vendido)
i_menos_vendido = vendas_ano.index(menos_vendido)

print(f"O melhor mês do ano foi {meses[i_mais_vendido]} com R${mais_vendido:,.1f}")
print(f"O pior mês do ano foi {meses[i_menos_vendido]} com R${menos_vendido:,.1f}")

faturamento = sum(vendas_ano)
percentual_mais_vendido = (mais_vendido / faturamento)

print(f"O faturamento anual foi de R${faturamento:,.2f} e o melhor mês do ano representou {percentual_mais_vendido:.1%} do faturamento.")
top3 = []
vendas_ano.sort(reverse=True)
print(vendas_ano)

maior_valor = max(vendas_ano)
top3.append(maior_valor)
print(top3)
vendas_ano.remove(maior_valor)
vendas_ano.sort(reverse=True)

print(vendas_ano)
seg_maior_valor = max(vendas_ano)
top3.append(seg_maior_valor)
print(top3)
vendas_ano.remove(seg_maior_valor)
vendas_ano.sort(reverse=True)

print(vendas_ano)
ter_maior_valor = max(vendas_ano)
top3.append(ter_maior_valor)
print(top3)
vendas_ano.remove(ter_maior_valor)
top3.sort(reverse=True)