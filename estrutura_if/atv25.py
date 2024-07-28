numero = int(input("Insira um numero:\n"))

if numero <= 10:
    print("O numero precisa ser maior que 10 para continuar:")
else:
    if numero < 20:
        total = numero * 2
        print("A multiplicação por 2 eh: %i" % total)
    else:
        total = numero * 5
        print("A multiplicação por 5 eh: %i" % total)
