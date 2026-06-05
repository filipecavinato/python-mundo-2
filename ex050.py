# Script criado por Filipe Cavinato

soma = 0
qt = 0

for i in range(1,7):
    n = int(input(f'Digite o {i}º número: '))

    if n % 2 == 0:
        soma += n
        qt += 1
if qt == 0:
    print('Você não digitou nenhum número par! A soma portanto vai ser 0!')
else:
    print(f'A soma dos {qt} números pares é igual a {soma}')
