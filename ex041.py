# Script criado por Filipe Cavinato

from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

print(f'Idade = {idade}')
print('Categoria')
if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infatil')
elif 14 < idade <= 19:
    print('Junior')
elif 19 < idade <= 20:
    print('Sênior')
else:
    print('Master')
