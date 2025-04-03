# Solicita os dados do produto
produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o preço unitário (R$): "))
quantidade = int(input("Digite a quantidade comprada: "))

# Calcula o valor total antes do desconto
valor_total = preco_unitario * quantidade

# Define o desconto de acordo com a quantidade
if quantidade < 10:
    percentual = 0
elif quantidade < 50:
    percentual = 0.05  # 5%
elif quantidade < 100:
    percentual = 0.10  # 10%
else:
    percentual = 0.15  # 15%

desconto = valor_total * percentual
valor_com_desconto = valor_total - desconto

print("Produto:", produto)
print("Valor total da compra: R$ {:.2f}".format(valor_total))
print("Valor do desconto: R$ {:.2f}".format(desconto))
print("Valor final da compra: R$ {:.2f}".format(valor_com_desconto))
