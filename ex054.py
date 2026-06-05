# Script criado por Filipe Cavinato

from datetime import date

cont = 0
for i in range(1,8):
    ano = int(input(f'Digite o ano de nascimento da {i}ª Pessoa: '))
    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade >= 21:
        cont += 1

print(f'{cont} pessoas já atingiram a maioridade!\n{7 - cont} ainda são menores de idade')
