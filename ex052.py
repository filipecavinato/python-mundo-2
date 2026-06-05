# Script criado por Filipe Cavinato

n = int(input('Digite um número: '))
div = 0
print('Divisões: ')
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[1;32m', i,'\033[m', end = '')
        div += 1
    else:
        print('\033[1;31m', i, '\033[m', end='')
print(f'\nO número foi divisível {div} vez(es)')
if div == 2:
    print(f'O número {n} é Primo!')
else:
    print(f'O número {n} não é Primo!')
