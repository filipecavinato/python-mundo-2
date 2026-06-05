# Script criado por Filipe Cavinato

print('-=-' * 7)
print('Progressão aritmetica')
print('-=-' * 7)

n1 = int(input('Digite o 1º Termo da Progressão: '))
r = int(input('Digite a Razão da Progressão: '))
ultimo = (n1 + (10 - 1) * r)
i = n1
qt = 1
total = 0
while i < (n1 + (10 -1) * r) + r:
    print(i, end=' -> ')
    i += r
    total += 1
print('Pausa')
while qt != 0:
    n1 = i
    qt = int(input('Quer que eu mostre mais quantos termos ? '))
    while i < (n1 + (qt - 1) * r) + r:
        print(i, end=' -> ')
        i += r
        total += 1
    if qt != 0:
        print('Pausa')
    else:
        print(f'Finalizando Progressão com {total} termos...')
print('FIM\n')
print('------ Fim do Programa ------')
