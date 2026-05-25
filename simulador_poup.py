#Simulador de Poupança--
aporte = float(input("Qunto você vai depositar por mês?"))
juros = float(input("Qual é a taxa de juros atual da poupança?"))
meses = int(input("Por quantos meses você vai investir?"))
juros_decimal = juros/100
total = 0
for mes in range(1, meses +1):
    total = total + aporte
    total = total +(total*juros_decimal)
    print(f"Mês{mes}: saldo total = R${total}")
print(f"Ao final de{meses}meses, você terá o valor de R$:{total:.2f}")