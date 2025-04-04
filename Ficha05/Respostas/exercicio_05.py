# Questão 05 - Rotação de Duplas no Coding Dojo do Grupy-Sanca

participantes = input("Digite os nomes separados por vírgula: ").split(",")
participantes = [p.strip() for p in participantes]

rodadas = int((2 * 60) / 5)
posicao = 0

for r in range(rodadas):
    copiloto = participantes[(posicao + 1) % len(participantes)]
    piloto = participantes[posicao % len(participantes)]
    print(f"Rodada {r+1}: {copiloto} (copiloto) e {piloto} (piloto)")
    posicao = (posicao + 1) % len(participantes)
