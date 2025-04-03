def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"


if __name__ == "__main__":
    try:
        peso = float(input("Digite seu peso em quilogramas: "))
        altura = float(input("Digite sua altura em metros: "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números para peso e altura.")
