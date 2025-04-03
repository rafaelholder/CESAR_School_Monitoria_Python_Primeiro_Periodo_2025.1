# Solicita o tempo de associação, a forma de pagamento e o valor da mensalidade
tempo = int(input("Digite o tempo de associação (em meses): "))
pagamento = input("Digite a forma de pagamento ('dinheiro' ou 'cartão'): ").strip().lower()
mensalidade = float(input("Digite o valor da mensalidade (R$): "))

# Define o percentual de desconto com base no tempo e na forma de pagamento
if tempo >= 12:
    if pagamento == "dinheiro":
        desconto_percentual = 0.15
    elif pagamento == "cartão":
        desconto_percentual = 0.10
    else:
        desconto_percentual = 0
        print("Forma de pagamento inválida.")
else:
    if pagamento == "dinheiro":
        desconto_percentual = 0.10
    elif pagamento == "cartão":
        desconto_percentual = 0.05
    else:
        desconto_percentual = 0
        print("Forma de pagamento inválida.")

valor_final = mensalidade - (mensalidade * desconto_percentual)

print("Valor da mensalidade após o desconto: R$ {:.2f}".format(valor_final))
