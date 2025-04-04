numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

media = sum(numeros) / len(numeros)
maior = max(numeros)
menor = min(numeros)

print("Média:", media)
print("Maior número:", maior)
print("Menor número:", menor)
