# Script criado por Filipe Cavinato

from time import sleep
from emoji import emojize

print('-=-' * 7)
print('Contagem Regressiva')
print('-=-' * 7)

for i in range(10, -1, -1):
    print(i)
    sleep(1)

print('Bum! Bum! Poow!', emojize(':fireworks: :fireworks: :fireworks: :fireworks: :fireworks:'))
