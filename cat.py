n = int(input())

string = [input().strip() for i in range(n)] #repete n vezes o input
string.sort(key=len) #organiza as strings por ordem de tamanho
formatar = "".join(string) #concatena uma lista de strings em uma unica string, "" informa que nao queremos nenhum separador

print(formatar)