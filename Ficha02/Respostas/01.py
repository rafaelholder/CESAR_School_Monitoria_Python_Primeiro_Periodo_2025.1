""" 
Uma loja online deseja implementar um sistema de cálculo de 
 desconto para suas  vendas. 
 O desconto varia de acordo com o valor total da compra e a 
 forma de  pagamento escolhida pelo cliente. 
"""

def calcularDesconto (valorOriginal, porcentagemDeDesconto):
    return valorOriginal * (porcentagemDeDesconto / 100)

desconto = 0 
valorCompra = float(input("Digite o valor da compra: "))
formaPagamento = input("Escolha a forma de pagamento(A Vista/A Prazo): ").lower()

if formaPagamento == "a vista":
    if valorCompra > 200.0:
        desconto = calcularDesconto(valorCompra)
    else:
        desconto = valorCompra * (5 / 100)
elif formaPagamento == "a prazo":
    if valorCompra > 100.0:
        desconto = valorCompra * (2 / 100)
        

valorFinalDaCompra = valorCompra - desconto
print(f"Valor original: {valorCompra} \nDesconto: {desconto}\nValor com desconto: {valorFinalDaCompra}")