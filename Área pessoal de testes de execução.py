nome = str(input("Digite seu nome: "))
email = input("Digite seu e-mail: ")

print(email.find("@"))

if nome and email:
    posicao = email.find("@")
    servidor = email[posicao:]
    if posicao != -1 and "." in servidor:
        print("Cadastro concluído!")
    else:
       print("Preencha os dados corretamente!")
else:
    print("Preencha os dados corretamente!")