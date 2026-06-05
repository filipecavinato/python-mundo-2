# Script criado por Filipe Cavinato

while True:
    n = int(input('Digite um número para ver a tabuada: '))
    if n < 0:
        print('-=-' * 14)
        break
    else:
        print(f'Tabuada do {n}')
        for i in range(1,11):
            print(f'{n} x {i:2} = {n * i}')
    print('-=-' * 14)
print('------ Fim do Programa ------')
