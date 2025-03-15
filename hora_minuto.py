# Escreva um programa que leia a hora de início e de fim de um evento e mostre
# o tempo do evento no formato HH:MM. A hora de início e fim é dada em minutos
# desde o início do dia.

inicio = int(input("inicio do evento: "))
fim = int(input("fim do evento: "))

total = fim - inicio
horas = total//60
minutos = total%60

print(f"{horas}:{minutos}")