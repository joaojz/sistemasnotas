primo = int(input("Digite um número:\n"))

divisoes = 0
contador = primo

while contador > 0:
    if primo % contador == 0:
        divisoes = divisoes + 1
    contador = contador - 1

if divisoes == 2:
    print("O número é primo")
else:
    print("O número não é primo")
