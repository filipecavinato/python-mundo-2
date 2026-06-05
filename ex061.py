# Script criado por Filipe Cavinato

print('-=-' * 7)
print('Progressão aritmetica')
print('-=-' * 7)

n1 = int(input('Digite o 1º Termo da Progressão: '))
r = int(input('Digite a Razão da Progressão: '))
i = n1
while i < (n1 + (10 -1) * r) + r:
    print(i, end=' -> ')
    i += r
print('FIM\n')
print('------ Fim do Programa ------')
