n = int(input())
variavel = 0

for i in range(n):
    x = input()

    if x == "++X" or x == "X++":
        variavel += 1
    elif x == "--X" or x == "X--":
        variavel -= 1

print(variavel)