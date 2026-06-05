# Script criado por Filipe Cavinato

from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

if idade < 18:
    print('Você ainda irá se alistar no exercito')
    print(f'Faltam {18 - idade} anos para o seu alistamento')
    print(f'Seu alistamento será em {ano + (18 - idade)}')
elif idade == 18:
    print('Já é hora de se alistar!')
    print('Procure a junta militar mais proxima de sua residencia!')
else:
    print('Já passou do prazo do alistamento')
    print(f'Passou {idade - 18} anos do prazo')
    print(f'Seu alistamento foi em {ano - (idade - 18)}')
