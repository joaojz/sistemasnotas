salario = float(input("Informe seu salario: "))
porcentagem = float(input("Infomer o valor de aumento de porcentagem: "))
novo_salario = salario * porcentagem/100
atual_salario = novo_salario + salario
print("Seu novo salario sera de R$%.3f" %atual_salario)