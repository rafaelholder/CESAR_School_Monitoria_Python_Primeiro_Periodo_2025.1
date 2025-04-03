# Define o ano atual (para fins do exercício, usamos 2025)
ano_atual = 2025

# Solicita o ano de nascimento
nascimento = int(input("Digite seu ano de nascimento: "))

# Calcula a idade
idade = ano_atual - nascimento

# Verifica a elegibilidade para votar
if idade < 16:
    mensagem = "Não pode votar"
elif (idade >= 16 and idade < 18) or (idade >= 70):
    mensagem = "Voto facultativo"
else:
    mensagem = "Voto obrigatório"

print("Idade:", idade)
print("Situação de voto:", mensagem)
