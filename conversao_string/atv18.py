conta_bancaria = 359.56
deposito =float(input("Informe o valor que sera depositado: "))
conta_bancaria2 = conta_bancaria + deposito
conta_bancaria3 = float(conta_bancaria2 - 125.98)
print("Foi descontado da sua conta o valor de R$ 125,98 reais, referente a fatura do seu cartão:")
print("Voce tem na sua conta R$%.2f Reais" %conta_bancaria3)