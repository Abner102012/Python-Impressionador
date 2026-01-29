meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]


for i, mes in enumerate(meses):
    print(f"Mês: {mes}. Temperatura: {temperaturas[i]}°C")

maior_temp = max(temperaturas)
indice_mais_quente = temperaturas.index(maior_temp)
mes_mais_quente = meses[indice_mais_quente]
print(f"O mês mais quente é {mes_mais_quente} com {maior_temp}°C.")

    