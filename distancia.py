# Escreva um programa que leia a distância entre duas cidades A e B, em kilômetros, a velocidade, em km/h, do carro e 
# mostre qual o tempo da viagem entre A e B, no formato HH:MM. Os segundos devem ser desprezados.

distancia = int(input())
velocidade = int(input())

horas = distancia//velocidade
minutos = int((distancia/velocidade - horas)*60)

print(f"{horas}:{minutos}")