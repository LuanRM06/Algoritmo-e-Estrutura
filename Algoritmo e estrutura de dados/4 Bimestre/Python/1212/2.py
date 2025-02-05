numero = []

for i in range(10):
    numunit = float(input("Insira um valor "))
    numero.append(numunit)
    
maior = 0

posicao = 0

for i in range(10):
    if numero[posicao] < numero[i]:
        maior = numero[i]
        posicao = i
        
        
print(f"O maior número foi {maior} na posicao {posicao} (OBS:começa em 0)")