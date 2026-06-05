# Script criado por Filipe Cavinato

soma = maior = menor = qt = 0
op = ''
while op != 'N':
    n = int(input(f'Digite o {qt + 1}º número: '))
    op = str(input('Quer continuar ? [S/N] ')).strip().upper()
    soma += n
    if qt == 0:
        menor = maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    qt += 1

print(f'Foram digitados {qt} valores')
print(f'O maior valor foi o {maior}\nO menor valor foi o {menor}\nA média entre todos é {soma/qt}\n')
print('------ Fim do Programa ------')
