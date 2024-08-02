saque = int(input("Insira valor do saque: "))
notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_1 = 0

while saque > 0:
    if saque >= 100:
        notas_100 += 1
        saque -= 100
    elif saque >= 50:
        notas_50 += 1
        saque -= 50
    elif saque >= 20:
        notas_20 += 1
        saque -= 20
    elif saque >= 10:
        notas_10 += 1
        saque -= 10
    else:
        notas_1 += 1
        saque -= 1

print(f"Você irá receber {notas_100} notas de 100, {notas_50} notas de 50, {notas_20} notas de 20, {notas_10} notas de 10, {notas_1} moedas de 1")
