# Script criado por Filipe Cavinato

n = qt = soma = 0
while n != 999:
    n = int(input(f'Digite o {qt + 1}º número [999 para parar]: '))
    if n != 999:
        qt += 1
        soma += n

print(f'Foram digitados {qt} números\nA soma de todos eles é {soma}')
print('------ Fim do Programa ------')
