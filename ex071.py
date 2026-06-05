# Script criado por Filipe Cavinato

print('---------------')
print('Banco CEV')
print('---------------')

v = int(input('Qual valor você quer sacar ? R$ '))
saque = [0, 0, 0, 0, 0, 0, 0]
notas = [100, 50, 20, 10, 5, 2, 1]
resto = v
i = 0
while True:
    for i in range(0, len(notas)):
        saque[i] = resto // notas[i]
        resto = resto % notas[i]
    break

for i in range(0,len(notas)):
    if saque[i] != 0:
        print(f'Total de {saque[i]} cédulas de R$ {notas[i]:.2f}')
print('--' * 17)
print('Volte Sempre ao Banco CEV! Tenha um otimo dia!')
print('\n------ Fim do Programa ------')
