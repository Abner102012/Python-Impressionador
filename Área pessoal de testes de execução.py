
lista_compras = {}

while True:
    print()                                     
    print("1 Adicionar item")
    print("2 Remover item")
    print("3 Ver lista")
    print("4 Sair")
    
    escolha = input("Escolha uma opção: ")
    escolha.strip()
    escolha.casefold()
    escolha.capitalize()
    if escolha == '1':
        item = input("Digite um item: ")
        valor = input("Digite o valor: ")
        lista_compras = [item, valor]
    elif escolha == '2':
        item = input("Digite um item: ")
        valor = input("Digite o valor: ")
        if item in lista_compras:
            del item, valor
    elif escolha == '3':
        print(lista_compras)
    elif escolha == '4':
        break
    else:
        print("Coloque os dígitos de 1 a 4")