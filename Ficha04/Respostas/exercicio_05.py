produto = 1
for numero in range(1, 16):
    if numero % 2 != 0:
        produto *= numero
print("O produto dos ímpares de 1 a 15 é:", produto)
