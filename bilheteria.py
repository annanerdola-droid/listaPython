#Aluno1:padronizar nome do filme
def formatar(nome):
    return nome.upper()
#Aluno2:verificador de idade
def verificar_idade(idade):
    if idade >= 18:
        return "Autorizado"
    else:
        return "Não autorizado"
#Aluno3:Mensagem de retorno
def gerar_mensagem(status):
    if status == "Autorizado":
        return "Tenha uma otima sessão!"
    else:
        return "sentimos, mas você não tem idade minima."
#Aluno4:Execução do Algoritmo
filme_entrada = input("Digite o filme Escolhido")
idade_entrada = int(input("Digite sua idade")
nome_final = formatar(filme_entrada)
status_acesso = verificar_idade(idade_entrada)
mensagem = gerar_mensagem(status_aceso)
print(f"\nfilme:{nome_final}")
print(f"status:{status_acesso}")
print(f"mensagem:{mensagem}")