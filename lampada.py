N = int(input())
numeros = list(input().replace(" ", ""))

lampadaA = False
lampadaB = False

for numero in numeros:
    if numero == "1":
        if lampadaA == False: # if not lampadaA;
            lampadaA = True
        elif lampadaA == True:
            lampadaA = False

    if numero == "2":
        if lampadaA == True:
            lampadaA = False
        elif lampadaA == False:
            lampadaA = True

        if lampadaB == False:
            lampadaB = True
        elif lampadaB == True:
            lampadaB = False

if lampadaA == True and lampadaB == True:
    print(1)
    print(1)
elif lampadaA == True and lampadaB == False:
    print(1)
    print(0)
elif lampadaA == False and lampadaB == True:
    print(0)
    print(1)
elif lampadaA == False and lampadaB == False:
    print(0)
    print(0)