# Script criado por Filipe Cavinato

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

if n1 > n2:
    print('O primeiro valor é maior')
    print(f'O número {n1} é maior que o {n2}')
elif n2 > n1:
    print('O segundo valor é maior')
    print(f'O número {n2} é maior que o {n1}')
else:
    print('Não existe valor maior, os números são iguais')
