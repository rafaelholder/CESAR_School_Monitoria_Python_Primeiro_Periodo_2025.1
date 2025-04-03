# Solicita a distância e o peso da carga
distancia = float(input("Digite a distância da entrega (km): "))
peso = float(input("Digite o peso da carga (kg): "))

# Cálculo do frete base (R$ 2,00 por km)
frete_base = distancia * 2.00

# Cálculo do custo adicional com base no peso
if peso <= 100:
    custo_peso = peso * 0.50
else:
    custo_peso = peso * 0.75

frete_total = frete_base + custo_peso

print("Valor total do frete: R$ {:.2f}".format(frete_total))
