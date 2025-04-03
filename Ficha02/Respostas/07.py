# Solicita as medidas dos três lados do triângulo
lado_a = float(input("Digite o valor do lado A: "))
lado_b = float(input("Digite o valor do lado B: "))
lado_c = float(input("Digite o valor do lado C: "))

# Verifica se as medidas formam um triângulo válido
if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
    # Classificação do triângulo
    if lado_a == lado_b == lado_c:
        tipo = "Equilátero"
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    print("Classificação do triângulo:", tipo)
else:
    print("As medidas não formam um triângulo válido.")
