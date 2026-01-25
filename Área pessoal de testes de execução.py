produtos = ["apple tv", "mac", "iphone x", "Ipad", "apple watch", "mac book", "airpods"]
print(produtos)
produtos.append("iphone 11")


item_removido = produtos.pop(2)
print(produtos)
print(f"Removemos o {item_removido} da lista.")