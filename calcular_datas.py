diainicial = int(input())
mesinicial = int(input())
diafinal = int(input())
mesfinal = int(input())

valido = True
if mesinicial < 1 or mesinicial > 12 or mesfinal < 1 or mesfinal > 12: 
    valido = False 

if valido:
    if mesinicial == 2:
        maxdiainicial = 28
    elif mesinicial in [4, 6, 9, 11]:
        maxdiainicial = 30
    else:
        maxdiainicial = 31

    if diainicial < 1 or diainicial > maxdiainicial:
        valido = False

    if mesfinal == 2:
        maxdiafinal = 28
    elif mesfinal in [4, 6, 9, 11]:
        maxdiafinal = 30
    else:
        maxdiafinal = 31

    if diafinal < 1 or diafinal > maxdiafinal:
        valido = False 

if not valido:
    print("Mês inválido")
else:
    if mesinicial == 1:
        total1 = diainicial
    elif mesinicial == 2:
        total1 = 31 + diainicial
    elif mesinicial == 3:
        total1 = 31 + 28 + diainicial
    elif mesinicial == 4:
        total1 = 31 + 28 + 31 + diainicial
    elif mesinicial == 5:
        total1 = 31 + 28 + 31 + 30 + diainicial
    elif mesinicial == 6:
        total1 = 31 + 28 + 31 + 30 + 31 + diainicial
    elif mesinicial == 7:
        total1 = 31 + 28 + 31 + 30 + 31 + 30 + diainicial
    elif mesinicial == 8:
        total1 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + diainicial
    elif mesinicial == 9:
        total1 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + diainicial
    elif mesinicial == 10:
        total1 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + diainicial
    elif mesinicial == 11:
        total1 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + diainicial
    else:  
        total1 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + diainicial

    if mesfinal == 1:
        total2 = diafinal
    elif mesfinal == 2:
        total2 = 31 + diafinal
    elif mesfinal == 3:
        total2 = 31 + 28 + diafinal
    elif mesfinal == 4:
        total2 = 31 + 28 + 31 + diafinal
    elif mesfinal == 5:
        total2 = 31 + 28 + 31 + 30 + diafinal
    elif mesfinal == 6:
        total2 = 31 + 28 + 31 + 30 + 31 + diafinal
    elif mesfinal == 7:
        total2 = 31 + 28 + 31 + 30 + 31 + 30 + diafinal
    elif mesfinal == 8:
        total2 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + diafinal
    elif mesfinal == 9:
        total2 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + diafinal
    elif mesfinal == 10:
        total2 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + diafinal
    elif mesfinal == 11:
        total2 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + diafinal
    else:  
        total2 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + diafinal

    if total2 < total1:
        print("A data final deve ser posterior à inicial.")
    else:
        print('Dias decorridos:', total2 - total1)
