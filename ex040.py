# Script criado por Filipe Cavinato

n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
media = (n1 + n2)/2

print(f'Média = {media:.2f}')
if media < 5:
    print('Reprovado')
elif 5 <= media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')
