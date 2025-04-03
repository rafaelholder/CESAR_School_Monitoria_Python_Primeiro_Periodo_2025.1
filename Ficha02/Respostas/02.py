# Solicita o nome do aluno e suas três notas
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Verifica a classificação
if media >= 7.0:
    classificacao = "Aprovado"
elif media >= 5.0:
    classificacao = "Recuperação"
else:
    classificacao = "Reprovado"

print("Aluno:", nome)
print("Média final: {:.2f}".format(media))
print("Classificação:", classificacao)
