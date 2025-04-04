soma_positivos = 0
quantidade_negativos = 0

for i in range(30):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero > 0:
        soma_positivos += numero
    elif numero < 0:
        quantidade_negativos += 1

print("Soma dos positivos:", soma_positivos)
print("Quantidade de negativos:", quantidade_negativos)
