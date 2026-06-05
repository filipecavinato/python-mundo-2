# Script criado por Filipe Cavinato

print('-=-' * 7)
print('Progressão aritmetica')
print('-=-' * 7)

n1 = int(input('Digite o 1º Termo da Progressão: '))
r = int(input('Digite a Razão da Progressão: '))

for i in range(n1, (n1 + (10 -1) * r) + r, r):
    print(i, end=' -> ')

print('FIM')
