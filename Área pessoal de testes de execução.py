produtos = [
    ("Mouse", 15),
    ("Teclado", 30),
    ("Monitor", 150),
    ("Headset", 12)
]

for produto, preco_dollar in produtos:
    preco_real = preco_dollar*5.26
    if preco_real > 100:
        print(f"{produto} custa R${preco_real:,.2f}")
        print(f"Já em dollar, o produto {produto} custa ${preco_dollar}")