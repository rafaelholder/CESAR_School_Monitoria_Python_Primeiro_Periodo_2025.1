# Solicita o salário anual
salario = float(input("Digite o salário anual (R$): "))

imposto = 0

if salario <= 20000:
    imposto = 0
elif salario <= 50000:
    imposto = salario * 0.10  # 10% de imposto
else:
    imposto = salario * 0.20  # 20% de imposto

print("Valor do imposto a ser pago: R$ {:.2f}".format(imposto))
