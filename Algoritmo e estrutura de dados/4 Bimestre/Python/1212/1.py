numero = []

for i in range(10):
    numunit = float(input("Insira uma nota "))
    numero.append(numunit)
    
qntd_negativo = 0
qntd_positivo = 0
    
for numunit in numero:
    if numunit < 0:
        qntd_negativo += 1
    if numunit > 0:
        qntd_positivo += 1
        
print (f"Foram inseridos: {qntd_negativo} números negativos e {qntd_positivo} números positivos")