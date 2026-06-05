# Script criado por Filipe Cavinato

from random import randint

qt = 0
comp_op = ''

print('Vamos jogar Par ou Impar!!')
while True:
    x = randint(0, 10)
    n = int(input('Diga um valor: '))
    while True:
        cond = str(input('Par ou Impar ? [P/I] ')).strip().upper()
        if cond in 'PI':
            break
    if cond == 'P':
        comp_op = 'I'
    elif cond == 'I':
        comp_op = 'P'
    else:
        print('Opção Invalida, digite [P/I]')
    if (n + x) % 2 == 0:
        print(f'Você jogou {n} e eu {x}. Total de {n + x} DEU PAR')
        if comp_op == 'P':
            print('Você PERDEU!')
            print('-=-' * 10)
            break
        else:
            print('Você GANHOU, vamos jogar novamente!')
            qt += 1
    else:
        print(f'Você jogou {n} e eu {x}. Total de {n + x} DEU ÍMPAR')
        if comp_op == 'I':
            print('Você PERDEU!')
            print('-=-' * 10)
            break
        else:
            print('Você GANHOU, vamos jogar novamente!')
            qt += 1
print(f'Game Over! Você venceu {qt} vezes')
print('------ Fim do Programa ------')
