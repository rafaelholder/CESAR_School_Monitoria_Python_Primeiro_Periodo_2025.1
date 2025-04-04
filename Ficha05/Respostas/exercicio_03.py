# Questão 03 - Simulação de Lançamento de Dados

import random

lancamentos = int(input("Digite o número de lançamentos: "))
contagem = [0] * 6

for _ in range(lancamentos):
    resultado = random.randint(1, 6)
    contagem[resultado - 1] += 1

for i in range(6):
    porcentagem = (contagem[i] / lancamentos) * 100
    print(f"Face {i+1}: {contagem[i]} vezes ({porcentagem:.2f}%)")

# Desafio: dois dados
print("\nCom dois dados:")
somas = {}

for _ in range(lancamentos):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    if soma in somas:
        somas[soma] += 1
    else:
        somas[soma] = 1

for soma in sorted(somas.keys()):
    porcentagem = (somas[soma] / lancamentos) * 100
    print(f"Soma {soma}: {somas[soma]} vezes ({porcentagem:.2f}%)")
