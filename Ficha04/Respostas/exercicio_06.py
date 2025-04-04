soma = 0
for numero in range(85, 908):
    if numero % 2 == 0:
        print(numero)
        soma += numero
print("Soma dos pares:", soma)
