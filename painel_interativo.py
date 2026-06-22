fila_espera=["Senha 01", "Senha 02", "Senha 03", "Senha 04"]
senha_atual = 0
while senha_atual < len(fila_espera):
    print("\n==========")
    print(f"Senha Atual:{fila_espera[senha_atual -1]}")
    if senha_atual > 0:
        prinr(f"Senha Anterior :")
            