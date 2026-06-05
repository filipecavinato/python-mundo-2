# Script criado por Filipe Cavinato

from random import randint

jokenpo = ['Pedra', 'Papel', 'Tesoura']

print('Vamos jogar jokenpô!')
op = str(input('Qual você quer escolher: ')).strip().capitalize()
comp = jokenpo[randint(0,2)]

print(f'Eu escolhi {comp}')

if comp == op:
    print('Empatamos!')
elif comp == 'Pedra':
    if op == 'Tesoura':
        print('Eu Ganhei!')
    elif op == 'Papel':
        print('Perdi! Você ganhou')
elif comp == 'Papel':
    if op == 'Pedra':
        print('Eu Ganhei!')
    elif op == 'Tesoura':
        print('Perdi! Você ganhou')
elif comp == 'Tesoura':
    if op == 'Pedra':
        print('Perdi! Você ganhou')
    elif op == 'Papel':
        print('Eu Ganhei!')
