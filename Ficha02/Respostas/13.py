# Solicita o tipo e o subtipo do produto
tipo = input("Digite o tipo do produto ('eletrônico', 'vestuário' ou 'livro'): ").strip().lower()
subtipo = input("Digite o subtipo do produto (ex: 'smartphone', 'camiseta', 'ficção'): ").strip().lower()

# Classifica o produto com base no tipo
if tipo == "eletrônico" or tipo == "eletronico":
    categoria = "Tecnologia"
elif tipo == "vestuário" or tipo == "vestuario":
    categoria = "Moda"
elif tipo == "livro":
    categoria = "Literatura"
else:
    categoria = "Outros"
    print("Tipo de produto inválido ou não reconhecido, classificado como 'Outros'.")

print("O produto é da categoria:", categoria)
