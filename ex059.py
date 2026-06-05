# Script criado por Filipe Cavinato

from time import sleep

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
op = 0

while op != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Verificar Maior
[4] Novos Números
[5] Sair do programa''')
    op = int(input('>>> Opção: '))
    if op == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif op == 2:
        print(f'A multiplicação de {n1} e {n2} é {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior é o {n1}')
        else:
            print(f'Entre {n1} e {n2} o maior é o {n2}')
    elif op == 4:
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção Invalida! Digite novamente')
    print('-=-' * 10)
    sleep(2)
print('------ Fim do Programa ------')
