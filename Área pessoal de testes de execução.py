produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

# Cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

qtde = 50000
preco = 40
total = qtde * preco
print(f"{total:,}")

if "livro" in produtos:
    i_livro = produtos.index("livro")
    produtos_ecommerce[i_livro][1] = produtos_ecommerce[i_livro][1] * 1.1
    print(produtos_ecommerce[i_livro][1])
else:
    pass