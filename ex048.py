# Script criado por Filipe Cavinato

soma = 0
qt = 0

for i in range(1,501):
    if i % 2 == 1 and i % 3 == 0:
        qt += 1
        soma += i

print(f'No intervalo solicitado temos {qt} números impares e múltiplos de 3')
print(f'Soma = {soma}')
