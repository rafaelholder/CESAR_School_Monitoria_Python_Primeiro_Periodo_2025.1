# Questão 02 - Fatorial e Soma de Dígitos

numero = input("Digite um número inteiro positivo: ")

if numero.isdigit() and int(numero) > 0:
    numero = int(numero)
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"Fatorial de {numero} é: {fatorial}")

    soma = 0
    pares = 0
    impares = 0
    produto = 1
    for digito in str(fatorial):
        d = int(digito)
        soma += d
        produto *= d
        if d % 2 == 0:
            pares += 1
        else:
            impares += 1

    media = soma / len(str(fatorial))

    print(f"Soma dos dígitos: {soma}")
    print(f"Dígitos pares: {pares}")
    print(f"Dígitos ímpares: {impares}")
    print(f"Produto dos dígitos: {produto}")
    print(f"Média dos dígitos: {media:.2f}")
else:
    print("Erro: Você deve digitar um número inteiro positivo.")
