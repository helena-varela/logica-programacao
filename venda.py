# Escreva um programa que leia o valor de um item a venda, a quantidade de
# itens que você vai comprar e o valor que você tem para pagar. Todos os valores
# são inteiros. O programa deve então informar o valor total a ser pago e o valor
# do troco que você vai receber

valor_item = int(input("Valor do item: "))
qnt_itens = int(input("Quantidade de itens: "))
dinheiro = int(input("Quanto você tem para pagar: "))

valor_total = valor_item*qnt_itens
troco = dinheiro - valor_total

print(f"O valor total será: {valor_total} \nTroco: {troco}")