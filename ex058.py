# Script criado por Filipe Cavinato

from random import randint
from time import sleep

print('Vou pensar em um número de 1 a 10\nTente acertar qual!!')
sleep(1)
print('Pensando', end = '')
for i in range(0,3):
    sleep(1)
    print('.', end = '')
sleep(1)
print('')

x = randint(1, 10)
num = 0
qt = 0
while num != x:
    qt += 1
    num = int(input(f'Palpite nº {qt}: '))
    if num != x:
        print(f'Não pensei no número {num}. Tenta denovo')
        if num < x:
            print('Tenta um número Maior.')
        else:
            print('Tenta um número Menor.')
print(f'Isso mesmo, eu pensei no número {x}!\nVocê acertou no {qt}º palpite\n')
print('------ Fim do Programa ------')
