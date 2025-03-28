casa_amigo = int(input())

passos = casa_amigo//5

if casa_amigo %5 != 0:
    passos += 1
    print(passos) 
else: 
    print(passos)   