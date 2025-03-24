# Lendo a entrada do exercício
n1, n2 = input().split() #split serve para separar o input nas duas variaveis de n1 e n2

media = (float(n1) + float(n2))/ 2 #transformar em float

# Seu código vai aqui

if media >= 7:
    print("Aprovado")
elif media < 7 and media >= 4:
    print("Recuperação")
else:
    print("Reprovado")