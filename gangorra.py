# Lendo a entrada do exercício
P1, C1, P2, C2 = map(int, input().split())
#1 = esquerdo 2 = direito
# Seu código vai aqui
esquerdo = P1 * C1 
direito = P2 * C2

if direito == esquerdo:
     print("0")
elif esquerdo > direito:
     print(-1)
elif direito > esquerdo:
     print(1)