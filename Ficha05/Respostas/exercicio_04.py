# Questão 04 – Agendamento de Pylestras Grupy-Sanca

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for hora in range(24):
    for minuto in range(60):
        if eh_primo(hora) and eh_primo(minuto):
            print(f"{hora:02}:{minuto:02}")
