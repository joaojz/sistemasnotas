print("Categoria 1: Bolsa\nCategoria 2:Tenis\nCategoria 3:Mochila")
categoria = int(input("Digite o numero da categoria desejada:\n"))
if categoria == 1:
    print("Bolsas")
elif categoria == 2:
    print("Tenis")
elif categoria == 3:
    print("Mochila")
else:
    print("Categoria nao encontrada!!")