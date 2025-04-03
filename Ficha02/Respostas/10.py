# Solicita o valor do imóvel e o tipo de imóvel
valor_imovel = float(input("Digite o valor do imóvel (R$): "))
tipo_imovel = input("Digite o tipo de imóvel ('residencial' ou 'comercial'): ").strip().lower()

comissao = 0

if tipo_imovel == "residencial":
    comissao = valor_imovel * 0.05
elif tipo_imovel == "comercial":
    comissao = valor_imovel * 0.03
else:
    print("Tipo de imóvel inválido.")

# Se o valor do imóvel for superior a R$ 500.000,00, adiciona 1% de bônus
if valor_imovel > 500000:
    bonus = valor_imovel * 0.01
    comissao += bonus

print("Valor da comissão: R$ {:.2f}".format(comissao))
