# Escreva um programa que leia a quantidade de dias desde o início do ano e
# mostre quantas semanas e quantos dias já se passaram desde do dia primeiro
# de janeiro

qnt_dias = int(input("quantos dias: "))

semanas = qnt_dias//7
dias = qnt_dias%7

print(f"{semanas} semana(s) e {dias} dia(s)")