#Etapa1-Cálculo do Imc
def calc_imc(peso,altura):
    imc = peso / (altura * altura)
    return imc
#Etapa2-Classificar o Imc
def classificar_imc(valor_imc):
    if valor_imc >= 25:
        return "ACIMA DO PESO"
    else:
        return "PESO NORMAL"
#Etapa3- Mensagem de Saída
def mensagem(status):
    if status == "ACIMA DO PESO":
        return "⚠️ATENÇÃO PROCURE UM MÉDICO"
    else:
        return "😁Você está no peso ideal!"
    #Etapa4- integração do projeto
    valor_peso= float(input("Digite seu peso atual: "))
    valor_altura = float(input("Digite sua altura: "))
    
    resultado = calc_imc(valor_peso, valor_altura)
    classificar = classificar_imc(resultado)
    saida = mensagem(classificar)

    print("=" * 50)
    print(f"Seu Imc é:({resultado:.1f}")
    print(f"{saida}")
    print("=" * 50)