nota = []

for i in range(5):
    notaunitaria = float(input("Insira uma nota"))
    nota.append(notaunitaria)
    
media = 0

for no in nota:
    media = media + no
    
media = media/5

print(f"A média geral é: {media}")