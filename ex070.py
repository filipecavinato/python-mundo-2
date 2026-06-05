# Script criado por Filipe Cavinato

prod = ['', 0.0]
barato = ['', 0.0]
maismil = 0
total = 0.0
print('--------------------')
print('Mercadinho Guanabara')
print('--------------------')
while True:
    nome = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$ '))
    if total == 0:
        barato[0] = nome
        barato[1] = preco
    total += preco
    if preco < barato[1]:
        barato[0] = nome
        barato[1] = preco
    if preco > 1000:
        maismil += 1
    while True:
        op = str(input('Quer continuar ? [S/N] ')).strip().upper()
        if op in 'SN':
            break
    if op == 'N':
        break
print(f'Total Gasto: R$ {total}\n{maismil} produtos custam mais de R$ 1.000,00')
print(f'Produto mais barato: {barato[0]} custando R$ {barato[1]:.2f}')
print('------ Fim do Programa ------')
