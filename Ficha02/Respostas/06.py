# Solicita o valor do consumo e o nível de satisfação
consumo = float(input("Digite o valor total do consumo (R$): "))
satisfacao = input("Digite o nível de satisfação (ótimo, bom ou ruim): ").strip().lower()

if satisfacao == "ótimo":
    gorjeta = consumo * 0.15
elif satisfacao == "bom":
    gorjeta = consumo * 0.10
elif satisfacao == "ruim":
    gorjeta = consumo * 0.05
else:
    gorjeta = 0
    print("Nível de satisfação inválido. Considerando gorjeta 0.")

total_conta = consumo + gorjeta

print("Valor da gorjeta: R$ {:.2f}".format(gorjeta))
print("Valor total da conta: R$ {:.2f}".format(total_conta))
