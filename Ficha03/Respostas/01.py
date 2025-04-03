def calcular_bonus(tempo_servico, meta_alcancada):
    bonus = 0
    # Bônus base para atingir a meta
    if meta_alcancada:
        bonus += 500
    # Bônus adicional para mais de 2 anos de serviço
    if tempo_servico >= 2:
        bonus += 200
    return bonus


if __name__ == "__main__":
    try:
        tempo = float(input("Digite o tempo de serviço (em anos): "))
        meta = input("O funcionário atingiu a meta de desempenho? (sim/não): ").strip().lower()
        meta_alcancada = meta in ['sim', 's', 'true', '1']
        
        total_bonus = calcular_bonus(tempo, meta_alcancada)
        print(f"Bônus total do funcionário: R$ {total_bonus:.2f}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número para o tempo de serviço.")
