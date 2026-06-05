# Script criado por Filipe Cavinato

print('-' * 9)
print('Fatorial')
print('-' * 9)
n = int(input('Digite um número: '))
c = n
fat = 1
print(f'O Fatorial de {n}! = ', end='')
while c != 0:
    fat *= c
    print(c, 'x ' if c > 1 else '= ', end='')
    c += -1
print(fat)

print('------ Fim do Programa ------')
