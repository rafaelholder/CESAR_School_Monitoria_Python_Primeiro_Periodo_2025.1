# Solicita o número de diárias e o tipo de quarto
diarias = int(input("Digite o número de diárias: "))
quarto = input("Digite o tipo de quarto ('standard', 'luxo' ou 'suíte'): ").strip().lower()

taxa = 0

if quarto == "standard":
    taxa = 10.00
elif quarto == "luxo":
    taxa = 15.00
elif quarto == "suíte" or quarto == "suite":
    taxa = 20.00
else:
    print("Tipo de quarto inválido.")

valor_total = diarias * taxa

print("Valor total da taxa de serviço: R$ {:.2f}".format(valor_total))
