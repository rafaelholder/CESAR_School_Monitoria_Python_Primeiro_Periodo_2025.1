# Solicita a renda mensal e a pontuação de crédito
renda = float(input("Digite sua renda mensal (R$): "))
credito = int(input("Digite sua pontuação de crédito: "))

if renda >= 2000 and credito >= 600:
    mensagem = "Elegível"
elif renda >= 1500 and credito >= 500:
    mensagem = "Elegível com restrições"
else:
    mensagem = "Não elegível"

print("Resultado da verificação: ", mensagem)
