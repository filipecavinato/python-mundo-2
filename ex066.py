# Script criado por Filipe Cavinato

qt = soma = 0
while True:
    n = int(input(f'Digite o {qt + 1}º número [999 para parar]: '))
    if n == 999:
        break
    qt += 1
    soma += n

print(f'Foram digitados {qt} números e a soma deles é {soma}')
print('------ Fim do Programa ------')
