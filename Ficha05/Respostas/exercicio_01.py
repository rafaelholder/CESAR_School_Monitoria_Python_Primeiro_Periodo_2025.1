# Questão 01 - Cálculo de Médias de Alunos

total_alunos = int(input("Digite o número de alunos: "))
soma_turma = 0
maior_media = -1
menor_media = 11
nome_maior = ""
nome_menor = ""
aprovados = 0
reprovados = 0

for i in range(total_alunos):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    num_notas = int(input(f"Quantas notas {nome} tem? "))
    soma = 0
    for j in range(num_notas):
        nota = float(input(f"Digite a nota {j+1} de {nome}: "))
        soma += nota
    media = soma / num_notas
    print(f"Média do aluno {nome}: {media:.2f}")
    soma_turma += media
    if media > maior_media:
        maior_media = media
        nome_maior = nome
    if media < menor_media:
        menor_media = media
        nome_menor = nome
    if media >= 7:
        aprovados += 1
    else:
        reprovados += 1

media_geral = soma_turma / total_alunos
print(f"Média da turma: {media_geral:.2f}")
print(f"Aluno com maior média: {nome_maior} ({maior_media:.2f})")
print(f"Aluno com menor média: {nome_menor} ({menor_media:.2f})")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")
