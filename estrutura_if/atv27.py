renda = float(input("Digite sua renda:\n"))
if renda < 2000:
    print("Seu limite eh de R$1.000 reais.")
elif renda > 2000 and renda < 4000:
    print("Seu limite eh de R$2.000 reais.")
elif renda > 4000 and renda < 6000:
    print("Seu limte eh de R$3.000 reais.")
elif renda > 10000:
    print("Entre em contato com o gerente!")
